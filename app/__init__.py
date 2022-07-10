from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import *
from werkzeug.security import *


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
    app.config['SECRET_KEY'] = 'SecretKey123'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .main import main
    app.register_blueprint(main)
    
    from .auth import auth
    app.register_blueprint(auth)
        
    return app

# from .main import main_bp
# app.register_blueprint(main_bp)

# if __name__ == '__main__':
#     app.run()