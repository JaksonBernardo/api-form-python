from flask import Flask
from config import Config
from flask_cors import CORS
from api.routes import register_routes
from api.extensions import init_extensions

def create_app():

    """Create a Flask application instance."""

    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5000", "http://127.0.0.1:5500"]}})
    init_extensions(app)
    register_routes(app)
    return app
