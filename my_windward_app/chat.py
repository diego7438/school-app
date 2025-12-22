from flask import Blueprint, render_template, request, jsonify
from .rotation import get_rotation_for_date
import datetime as dt

bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route('/')
def index():
    return render_template('chat.html')

@bp.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    message = data.get('message', '').lower()

    # default response
    response = "I'm just a baby AI 🦁. I only know about today's schedule right now. Try asking 'What is the rotation today?'"

    # simple keyword matching (the "brain")
    if 'hello' in message or 'hi' in message:
        response = "Hello! I'm the Windward Bot. Ask me about the schedule!"

    elif 'today' in message:
        now = dt.datetime.now()
        info = get_rotation_for_date(now.month, now.day)
        if info:
            response = f"Today ({now.strftime('%B %d')}) is a Rotation {info[0]} day ({info[1].upper()})."
        else:
            response = "There is no school today. Enjoy the day off!"

    return jsonify({'response': response})