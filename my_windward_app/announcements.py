from flask import (
    Blueprint, request, jsonify, render_template, g
)
from .db import get_db_connection # the '. means import from the same package

# create the blueprint. 'announcements' is the name of this blueprint
bp = Blueprint('announcements', __name__)

@bp.route('/', methods=['GET', 'POST'])
def handle_announcements():
    conn = get_db_connection()

    if request.method == 'POST':
        # security check: only teachers can post
        if g.user is None or g.user['role'] != 'teacher':
            return jsonify({"error": "Only teachers can post announcements."}), 403
        
        new_announcement = request.get_json()
        # we automatically set the author to the logged-in user
        author = g.user['username']
        message = new_announcement['message']

        conn.execute('INSERT INTO announcements (author, message) VALUES (?, ?)', 
                     (author, message))
        conn.commit()
        conn.close()
        return jsonify({"message": "Announcement posted succesfully!"}), 201
    
    # the GET request
    posts = conn.execute('Select * FROM announcements ORDER BY created DESC').fetchall()
    conn.close()

    # instead of returning raw JSON, we render a nice HTML page
    return render_template('announcements.html', posts=posts)