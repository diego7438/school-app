from flask import Blueprint, render_template, request, redirect, url_for
from .auth import login_required, role_required
from .db import get_db_connection

# create a new blueprint for teacher-specific routes
bp = Blueprint('teacher', __name__, url_prefix='/teacher')

@bp.route('/dashboard')
@login_required
@role_required('teacher') # make it so only teachers can enter
def dashboard():
    """
    Render the Teacher Dashboard.
    Fetches all users with the 'student' role to display in a roster.
    """
    db = get_db_connection()
    # get all users who are students
    # We filter by role='student' so teachers don't see other teachers in the list
    students = db.execute(
        "SELECT * FROM users WHERE role = 'student'"
    ).fetchall()

    return render_template('teacher_dashboard.html', students=students)

@bp.route('/grade', methods=['POST'])
@login_required
@role_required('teacher')
def update_grade():
    """
    Handle form submission to update a student's grade.
    Redirects back to the dashboard after saving.
    """
    user_id = request.form['user_id']
    grade = request.form['grade']

    db = get_db_connection()
    # SQL Update command to save the new grade for the specific user ID
    db.execute(
        'UPDATE users SET grade = ? WHERE id = ?',
        (grade, user_id)
    )

    db.commit()

    return redirect(url_for('teacher.dashboard'))