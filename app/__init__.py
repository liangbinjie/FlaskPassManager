from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SECRET_KEY'] = 'SecretKey123'

    db.init_app(app)

    from .main import main_bp
    app.register_blueprint(main_bp)
    
    
    return app

# from .main import main_bp
# app.register_blueprint(main_bp)

# if __name__ == '__main__':
#     app.run()