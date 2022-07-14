from flask import *
from flask_login import *
from .models import Passwords
from . import db

main = Blueprint('main', __name__)


@main.route('/home')
@login_required
def index():
    user_pass = current_user.passwords
    return render_template('home.html', passwords=user_pass)


@main.route("/add")
@login_required
def add():
    return render_template('config/add.html')


@main.route("/add", methods=['POST'])
@login_required
def add_post():
    title = request.form['title']
    password = request.form['password']
    url = request.form['url']
    username = request.form['username']
    email = request.form['email']

    new_pass = Passwords(title=title, password=password, url=url, email=email, username=username, user_id=current_user.id)
    db.session.add(new_pass)
    db.session.commit()

    return redirect(url_for('main.index'))


@main.route("/delete/<int:id>", methods=['POST', 'GET'])
@login_required
def delete(id):
    row = Passwords.query.filter_by(id=id).first()
    db.session.delete(row)
    db.session.commit()
    return redirect(url_for('main.index'))