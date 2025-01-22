from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load configuration
    app.config.from_object("app.config.Config")

    # Initialize extensions
    db.init_app(app)

    # Register routes
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)
        db.create_all()

    return app
