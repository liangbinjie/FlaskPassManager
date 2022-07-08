from flask import *

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def index():
    return render_template('base.html')


@main_bp.route("/user")
def user():
    return "User"