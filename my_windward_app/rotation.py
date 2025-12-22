import datetime as dt
from flask import Blueprint, jsonify, render_template

# Now that the data files are in the same package, we can import them directly.
from . import weekly_rotation_data

# Create the Blueprint for the rotation feature
bp = Blueprint('rotation', __name__, url_prefix='/api/rotation')

ROTATIONS = weekly_rotation_data.weekly_rotations
DAY_NAME = ["mon", "tue", "wed", "thu", "fri"]

def get_year_from_schedule(m):
    """Determine the year (2025 or 2026) based on the month for the 25-26 school year."""
    if m < 8: return 2026
    else: return 2025

def within_a_week_of(m1, d1, m2, d2):
    """Check if date2 is within the same calendar week as date1."""
    year_date1 = get_year_from_schedule(m1)
    year_date2 = get_year_from_schedule(m2)
    date1 = dt.date(year_date1, m1, d1)
    date2 = dt.date(year_date2, m2, d2)
    time_difference = date2 - date1
    return 0 <= time_difference.days < 7

def get_week_rotation(m, d):
    """Find the rotation schedule entry for the week containing the given date."""
    for idx, (month, date, blocks, off) in enumerate(ROTATIONS):
        if within_a_week_of(month, date, m, d):
            return ROTATIONS[idx]
    return None

def get_rotation_for_date(m, d):
    """
    Main logic to determine the specific rotation day (1-6) for a specific date.
    Handles weekends, holidays, and special schedules.
    """
    # 1. Find which week this date belongs to
    # We loop through the master schedule to find the week starting near this date
    rotations = get_week_rotation(m, d)
    if rotations is None:
        return None

    # 2. Unpack the data for that week
    # blocks is the list of rotation days (e.g., [1, 2, 3, 4, 5])
    month, date, blocks, days_off = rotations
    
    # 3. Handle days off (insert None into the schedule)
    # We create a copy of the blocks so we don't modify the original data
    adjusted_blocks = list(blocks)
    if days_off is not None:
        if isinstance(days_off, int):
            adjusted_blocks.insert(days_off - 1, None)
        elif isinstance(days_off, list):
            for day_index in sorted(days_off):
                adjusted_blocks.insert(day_index - 1, None)

    # 4. Calculate which day of the week it is (0=Mon, 1=Tue, etc.)
    # We use datetime objects to calculate the exact number of days from the start of the week
    year_date2 = get_year_from_schedule(m)
    year_date1 = get_year_from_schedule(month)
    date2 = dt.date(year_date2, m, d)
    date1 = dt.date(year_date1, month, date)
    days_diff = (date2 - date1).days

    # 5. Safety checks
    if days_diff < 0 or days_diff > 4:
        return None # It's a weekend or out of range
    
    if days_diff >= len(adjusted_blocks):
        return None # Should not happen if data is correct

    return (adjusted_blocks[days_diff], DAY_NAME[days_diff])

# --- The API Endpoint ---
@bp.route('/')
def index():
    return render_template('rotation.html')

@bp.route("/<int:month>/<int:day>")
def api_get_rotation(month, day):
    try:
        rotation_info = get_rotation_for_date(month, day)

        if rotation_info and rotation_info[0] is not None:
            # Return the rotation number and the day name (e.g., "MON")
            result = {"rotation": rotation_info[0], "day_of_week": rotation_info[1]}
            return jsonify(result)
        else:
            # This handles days off or weekends
            error_message = {"error": "No school or rotation found for this date."}
            return jsonify(error_message), 404
            
    except Exception as e:
        # This prints the actual error to your terminal so we can see it!
        print(f"SERVER ERROR: {e}")
        return jsonify({"error": f"Server Error: {str(e)}"}), 500
