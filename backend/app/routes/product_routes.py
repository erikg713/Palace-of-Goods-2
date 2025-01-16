from flask import Blueprint
from app.controllers.product_controller import add_product, get_products

product_bp = Blueprint('product', __name__)

product_bp.route('/', methods=['POST'])(add_product)
product_bp.route('/', methods=['GET'])(get_products)
