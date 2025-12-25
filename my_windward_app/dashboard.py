from flask import (
    Blueprint, render_template, g
)

from .auth import login_required
bp = Blueprint('dashboard', __name__, url_prefix= '/dashboard')

@bp.route('/')
@login_required
def index():
    # In the future, we will calculate the rotation day here!
    return render_template('dashboard.html')