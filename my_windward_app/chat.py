from flask import Blueprint, render_template, request, jsonify
from .rotation import get_rotation_for_date
import datetime as dt

bp = Blueprint('chat', __name__, url_prefix='/chat')

def get_next_day_of_week(day_name):
    """
    Calculates the date of the next occurrence of a given day of the week.
    For example, if today is Wednesday and day_name is 'friday', it returns this Friday's date.
    If day_name is 'monday', it returns next Monday's date.
    """
    today = dt.date.today()
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                    'saturday', 'sunday']
    try:
        target_day_index = days_of_week.index(day_name.lower())
    except ValueError:
        return None # The provided day_name wasn't a real day
    
    days_ahead = target_day_index - today.weekday()
    if days_ahead <= 0: # target day has already passed this week
        days_ahead += 7

    return today + dt.timedelta(days=days_ahead)

@bp.route('/')
def index():
    return render_template('chat.html')

@bp.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    message = data.get('message', '').lower()

    # Default response
    response = "I'm not advanced enough to understand that yet 🦁. " \
    "Try asking about 'today', 'tomorrow', or a day of the week like 'monday'."


    # --- This is the AI's "Brain" ---
    # It's a series of checks (if/elif/else) to figure out the user's "intent".

    # Intent: Greeting
    if 'hello' in message or 'hi' in message:
        response = "Hello! I'm the Windward Bot. Ask me about the schedule!"

    # Intent: Tomorrow's Schedule
    elif 'tomorrow' in message:
        # Get tomorrow's date object
        target_date = dt.date.today() + dt.timedelta(days = 1)
        # Ask our rotation logic for the schedule for that date
        info = get_rotation_for_date(target_date.month, target_date.day)
        # The 'info' variable is a tuple like (6, "tue") or None if there's no school.
        if info and info[0] is not None:
            # Use an f-string to build a nice response.
            # info[0] is the rotation number, info[1] is the day name.
            response = f"Tomorrow ({target_date.strftime('%B %d')}) is a Rotation {info[0]} day ({info[1].upper()})."
        else:
            response = "There is no school tomorrow. Enjoy!"

    # Intent: Today's Schedule
    elif 'today' in message:
        target_date = dt.date.today()
        info = get_rotation_for_date(target_date.month, target_date.day)
        if info and info[0] is not None:
            response = f"Today ({target_date.strftime('%B %d')}) is a Rotation {info[0]} day ({info[1].upper()})."
        else:
            response = "There is no school today. Enjoy the day off!"

    # Intent: Future Day of the Week
    else: # If it's not about today or tomorrow, check if they mentioned a day of the week.
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        for day in days:
            if day in message:
                # If we find a day (e.g., "monday"), calculate the date for the upcoming Monday.
                target_date = get_next_day_of_week(day)
                if target_date:
                    info = get_rotation_for_date(target_date.month, target_date.day)
                    if info and info[0] is not None:
                        response = f"This coming {day.capitalize()} ({target_date.strftime('%B %d')}) will be a Rotation {info[0]} day."
                    else:
                        response = f"There is no school this coming {day.capitalize()}."
                break # Important: We stop after finding the first day mentioned to avoid confusion.

    return jsonify({'response': response})