from flask import Blueprint, render_template, request, jsonify
from .rotation import get_rotation_for_date
import datetime as dt
import pytz
import re

bp = Blueprint('chat', __name__, url_prefix='/chat')

# Pre-compile regex patterns for efficiency
DATE_PATTERN = re.compile(r'(january|february|march|april|may|june|july|august|september|october|november|december)\s+(\d{1,2})')
SHORT_DATE_PATTERN = re.compile(r'\b(\d{1,2})/(\d{1,2})\b')

MONTHS = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

def get_next_day_of_week(day_name, today):
    """
    Calculates the date of the next occurrence of a given day of the week.

    Args: 
        day_name (str): The name of the day (e.g., 'monday').
        today (datetime.date): The reference date to start counting from. 

    Returns:
        datetime.date: The date object for the upcoming day. 
    
    """
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
    """
    Processes user messages and returns a JSON response.

    Features: 
    - Input sanitization (length checks, type checks).
    - Timezone awareness (converts server time to LA time).
    - Intent recognition via keyword matching and Regex. 

    """
    # Security: Ensure request is JSON
    if not request.is_json:
        return jsonify({'error': 'Invalid Content-Type'}), 400

    data = request.get_json()
    message = data.get('message', '')

    # Security: Input sanitization and length limit
    if not isinstance(message, str):
        return jsonify({'response': "Please send text."})
    if len(message) > 200:
        return jsonify({'response': "Message too long. Please keep it under 200 characters."})

    message = message.lower().strip()

    # Efficiency/Accuracy: Use correct Timezone (LA Time)
    tz = pytz.timezone('America/Los_Angeles')
    today = dt.datetime.now(tz).date()

    # Default response
    response = "I'm not advanced enough to understand that yet 🦁. " \
    "Try asking about 'today', 'tomorrow', a specific date like 'August 25', or a day of the week."


    # --- This is the AI's "Brain" ---
    # It's a series of checks (if/elif/else) to figure out the user's "intent".

    # Intent: Greeting
    if 'hello' in message or 'hi' in message:
        response = "Hello! I'm the Windward Bot. Ask me about the schedule!"

    # Intent: Tomorrow's Schedule
    elif 'tomorrow' in message:
        # Get tomorrow's date object using LA time
        target_date = today + dt.timedelta(days = 1)
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
        target_date = today
        info = get_rotation_for_date(target_date.month, target_date.day)
        if info and info[0] is not None:
            response = f"Today ({target_date.strftime('%B %d')}) is a Rotation {info[0]} day ({info[1].upper()})."
        else:
            response = "There is no school today. Enjoy the day off!"

    # Intent: Specific Date (e.g. "August 25" or "8/25")
    # We use the walrus operator (:=) to assign the match and check it in one line
    elif (match := DATE_PATTERN.search(message)) or (match := SHORT_DATE_PATTERN.search(message)):
        groups = match.groups()
        # Check if first group is a month name or a number
        if groups[0] in MONTHS:
            m = MONTHS[groups[0]]
            d = int(groups[1])
        else:
            m = int(groups[0])
            d = int(groups[1])
        
        # Get rotation
        info = get_rotation_for_date(m, d)
        if info and info[0] is not None:
            response = f"On {m}/{d}, it is a Rotation {info[0]} day ({info[1].upper()})."
        else:
            response = f"There is no school on {m}/{d}."

    # Intent: Future Day of the Week
    else: # If it's not about today or tomorrow, check if they mentioned a day of the week.
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        found_day = False
        for day in days:
            if day in message:
                # If we find a day (e.g., "monday"), calculate the date for the upcoming Monday.
                # We pass 'today' to ensure timezone consistency
                target_date = get_next_day_of_week(day, today)
                if target_date:
                    info = get_rotation_for_date(target_date.month, target_date.day)
                    if info and info[0] is not None:
                        response = f"This coming {day.capitalize()} ({target_date.strftime('%B %d')}) will be a Rotation {info[0]} day."
                    else:
                        response = f"There is no school this coming {day.capitalize()}."
                found_day = True
                break 
        
        if not found_day:
            # If we still don't know, keep the default response
            pass

    return jsonify({'response': response})