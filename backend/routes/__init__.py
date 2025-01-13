from flask import Blueprint

# Initialize the blueprint
routes_bp = Blueprint('routes', __name__)

# Import all route modules
from .user_routes import *
from .product_routes import *
from .order_routes import *

# Register routes to the blueprint
# Note: Ensure each route module defines its routes