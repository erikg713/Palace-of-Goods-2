from flask import Blueprint

# Import blueprints from other files
from app.routes.product_routes import product_bp
from app.routes.order_routes import order_bp
from app.routes.payment_routes import payment_bp

# Create a main blueprint
main = Blueprint('main', __name__)

# Register blueprints
main.register_blueprint(product_bp, url_prefix='/products')
main.register_blueprint(order_bp, url_prefix='/orders')
main.register_blueprint(payment_bp, url_prefix='/payments')
