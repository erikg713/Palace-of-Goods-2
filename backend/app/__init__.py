from flask import Flask
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "your-secret-key"

    # Initialize JWT
    jwt = JWTManager(app)

    # Register blueprints
    from app.routes.admin_routes import admin_bp
    app.register_blueprint(admin_bp)

    return app
