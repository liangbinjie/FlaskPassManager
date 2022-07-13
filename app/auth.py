from flask import *
from flask_login import *
from .models import User
from . import db
from werkzeug.security import check_password_hash, generate_password_hash


auth = Blueprint('auth', __name__)

@auth.route("/")
def login():
    # from .models import User
    
    # new_user = User(username="admin", password=generate_password_hash("admin12345"))
    # db.session.add(new_user)
    # db.session.commit()
    return render_template('index.html')


@auth.route("/", methods=['POST'])
def login_post():

    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username.lower()).first()

    if not user:
        flash('User doesn\'t exists')
        return redirect(url_for('auth.login'))

    elif not check_password_hash(user.password, password):
        flash('Incorrect password, try again.')
        return redirect(url_for('auth.login'))



    login_user(user)
    return redirect(url_for('main.index'))



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/changeUser")
@login_required
def changeUser():
    user = current_user.username
    
    return render_template('auth/change.html', username = user)


@auth.route("/changeUser", methods=['POST'])
@login_required
def changeUserPOST():
    
    user = request.form['username']
    current_pass = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    if request.method == 'POST':
        if check_password_hash(current_user.password, current_pass):
            if new_password == confirm_password:
                current_user.username = user
                current_user.password = generate_password_hash(new_password)
            else:
                flash("Passwords don't match")
                return redirect(url_for('auth.changeUser'))
        
        else:
            flash("Current password is incorrect")
            return redirect(url_for('auth.changeUser'))

        db.session.commit()
        logout_user()
        return redirect(url_for('auth.login'))


    
