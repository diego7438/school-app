import functools
from flask import (
    Blueprint, request, jsonify, session, g, render_template
)

# this is a library that helps us hash passwords
from werkzeug.security import generate_password_hash, check_password_hash

from .db import get_db_connection

# create the Blueprint for authentication
bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    # a decorator to protect views that require a login
    # This wraps the view function and checks if a user is logged in before running it
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
        # if no user is logged in, return a 401 Unathorized error
            return jsonify({"error": "Authentication required."}), 401
    
    # if a user is logged in, call the original view function
        return view(**kwargs)
    return wrapped_view

def role_required(role):
    # a decorator (bouncer) to protect views that require certain roles.
    # Usage: @role_required('teacher')
    def decorator(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            # first gotta ensure the user is logged in at all.
            if g.user is None:
                return jsonify({"error": "Authentication required"}), 401
            # then check if they have the required role.
            if g.user['role'] != role:
                return jsonify({"error": "Insufficient permissions. "
                "This resource requires a '" + role + "' role."}), 403 # 403 is "forbidden"
            return view(**kwargs)
        return wrapped_view
    return decorator


@bp.before_app_request
def load_logged_in_user():
    # if a user id is stored in the session, load the user object from the database
    # This runs before every single request to checking who is visiting
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        # get the user from the database and store it in g.user for this request
        g.user = get_db_connection().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # get the username and password from the JSON data sent by the user
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        role = data.get('role') # allow role to be optionally provided
        db = get_db_connection()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        if error is None:
            try:
                # attempt to insert the new user into the database
                # we store the HASH of the password, never the password itself.
                # pbkdf2:sha256 is a strong hashing algorithm provided by Werkzeug
                # if a role is provided, we insert it, otherwise the DB default is used.
                cursor = None
                if role: 
                    cursor = db.execute(
                        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                        (username, generate_password_hash(password, method='pbkdf2:sha256'), role),
                    )
                else:
                    cursor = db.execute(
                        "INSERT INTO users (username, password) VALUES (?, ?)",
                        (username, generate_password_hash(password, method='pbkdf2:sha256')),
                    )
                db.commit()
                
                # Auto-login: Clear session and set the new user_id
                session.clear()
                session['user_id'] = cursor.lastrowid
            except db.IntegrityError:
                # this error only occurs if the username already exists
                error = f"User {username} is already registered"
            else:
                # if everything was successful, return a success message
                return jsonify({"message": f"User {username} created successfully."}), 201
        
        # if there was an error at any point, return an error message
        return jsonify({"error": error}), 400
    # if its a GET request, just show the registration page
    return render_template('register.html')

@bp.route('/login', methods=['POST'])
def login():
    # get the username and password from the JSON data
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    db = get_db_connection()
    error = None

    # query the database to find the user by their username
    # the comma in (username,) is important bc it makes it a tuple
    user = db.execute(
        'SELECT * FROM users WHERE username = ?', (username,)
    ).fetchone() # fetchone() gets one result from the query

    if user is None:
        # if no user is found with that username, set an error
        error = 'Incorrect username.'
    elif not check_password_hash(user['password'], password):
        # if the user is found, check the provided password's hash
        # matches the stored hash
        error = 'Incorrect password.'

    if error is None:
        # if there are no error, the login is successful.
        # clear the session and store the new user's id.
        # this is our "digital hall pass".
        session.clear()
        session['user_id'] = user['id']

        # If "Remember Me" was checked, make the session permanent (lasts 31 days by default)
        if data.get('remember') == 'on':
            session.permanent = True

        return jsonify({"message": "Login successful :)."}), 200
    
    # but if there was an error, return it
    return jsonify({"error": error}), 401 # 401 is the unathourized status code

@bp.route('/logout', methods=['POST'])
def logout():
    # clear the current session, including the user_id
    session.clear()
    return jsonify({"message": "Logout successful."}), 200
