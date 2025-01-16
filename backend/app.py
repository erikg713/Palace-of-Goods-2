from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from flask_migrate import Migrate
migrate = Migrate(app, db)

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp
    from app.routes.order_routes import order_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(order_bp, url_prefix='/api/orders')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
