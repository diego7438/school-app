from flask import (
    Blueprint, render_template, g
)

import datetime as dt
import pytz
from .rotation import get_rotation_for_date
from .auth import login_required

bp = Blueprint('dashboard', __name__, url_prefix= '/dashboard')

@bp.route('/')
@login_required
def index():
    # Get today's date in Pacific Time (Windward School location)
    tz = pytz.timezone('America/Los_Angeles')
    today = dt.datetime.now(tz).date()

    # Get the rotation info: returns (rotation_number, day_name) or None
    rotation_info = get_rotation_for_date(today.month, today.day)

    return render_template('dashboard.html', rotation=rotation_info, date=today)