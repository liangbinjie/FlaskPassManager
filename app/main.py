from flask import *

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def index():
    return "hello world"