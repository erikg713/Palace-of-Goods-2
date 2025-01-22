from flask import Flask
from app.routes.auth_routes import auth_bp
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your-secret-key"

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")

    return app
