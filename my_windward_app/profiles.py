from flask import Blueprint, jsonify, g, render_template

# we need our new bouncer from the auth blueprint
from .auth import login_required, role_required

# create the blueprint for the profiles feature
bp = Blueprint('profiles', __name__, url_prefix='/api/profile')

# the route is not at the root ('/') because the '/api/profile'
# part is handled by the url_prefix in the Blueprint definition
@bp.route("/", methods=['GET'])
@login_required # this is the new bouncer in action
def get_profile():
    # because of @login_required, we know g.user is set.
    # we can now return the logged_in user's info.
    # note: we don't want to send the password hash back to the client.
    user_profile = {
        "id": g.user['id'],
        "username": g.user['username'],
        "role": g.user['role']
    }
    # instead of returning json, render the new profile.html template
    return render_template('profile.html', user=user_profile)

@bp.route("/teacher-dashboard", methods=['GET'])
@role_required('teacher') # our new bouncer, checking for the 'teacher' role :)
def get_teacher_dashboard():
    # instead of json, render the new dashboard template.
    return render_template('teacher_dashboard.html')