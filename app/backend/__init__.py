from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='../frontend/build')
    cors = CORS(app)

    from .routes import main
    app.register_blueprint(main)

    return app