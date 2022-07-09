from flask import Flask


app = Flask(__name__)


def create_app():
    
    from .main import main_bp
    app.register_blueprint(main_bp)
    
    
    return app
# from .main import main_bp
# app.register_blueprint(main_bp)

# if __name__ == "__main__":
#     app.run()