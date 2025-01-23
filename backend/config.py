# config.py
import os

class Config:
    """
    Flask configuration class for managing app settings, SQLAlchemy, and JWT.
    """

    # Flask application settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']
    TESTING = os.getenv('TESTING', 'False').lower() in ['true', '1', 't']

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-jwt-secret-key')

    # Additional Flask configurations
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'True').lower() in ['true', '1', 't']
    PERMANENT_SESSION_LIFETIME = int(os.getenv('SESSION_LIFETIME', 3600))  # Default to 1 hour

    # CORS settings (optional)
    CORS_HEADERS = os.getenv('CORS_HEADERS', 'Content-Type')

# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)

    # Load configurations
    app.config.from_object('config.Config')

    # Initialize extensions with app
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Register routes or blueprints
    @app.route('/')
    def index():
        return "Welcome to the Flask app!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
