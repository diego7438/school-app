from flask import (
    Blueprint, render_template, g
)

import datetime as dt
from .rotation import get_rotation_for_date
from .auth import login_required

bp = Blueprint('dashboard', __name__, url_prefix= '/dashboard')

@bp.route('/')
@login_required
def index():
    # Get today's date
    today = dt.date.today()

    # Get the rotation info: returns (rotation_number, day_name) or None
    rotation_info = get_rotation_for_date(today.month, today.day)

    return render_template('dashboard.html', rotation=rotation_info, date=today)