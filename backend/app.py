from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_talisman import Talisman
from config import config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(get_remote_address, app=None)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    limiter.init_app(app)
    # Other initializations...
    return app

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    Talisman(app, content_security_policy=None)

    # Register blueprints
    from routes.auth_routes import auth_bp
    from routes.item_routes import item_bp
    from routes.payment_routes import payment_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(item_bp, url_prefix='/api/items')
    app.register_blueprint(payment_bp, url_prefix='/api/payments')

    return app