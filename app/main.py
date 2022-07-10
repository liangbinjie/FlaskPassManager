from flask import *
from flask_login import *

main = Blueprint('main', __name__)


@main.route('/home')
@login_required
def index():
    return render_template('base.html')


@main.route("/user")
def user():
    return "User"

