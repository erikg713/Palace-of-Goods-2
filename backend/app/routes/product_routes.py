from flask import Blueprint, jsonify, request
from app.models import db, Product
from flask_jwt_extended import jwt_required
from app.exceptions import ProductNotFoundError
from sqlalchemy.exc import SQLAlchemyError

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    """
    Get a list of products based on query parameters.

    Query Parameters:
        query (str): The search query for product names.
        page (int): The page number for pagination.
        per_page (int): The number of items per page.

    Returns:
        Response: A JSON response containing the list of products.
    """
    try:
        query = request.args.get('query', '').strip()
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        if page <= 0 or per_page <= 0:
            return jsonify({'error': 'Page and per_page must be positive integers.'}), 400

        products = Product.query.filter(Product.name.ilike(f"%{query}%")).paginate(page, per_page, False)
        return jsonify([product.to_dict() for product in products.items])
    except ValueError:
        return jsonify({'error': 'Invalid pagination parameters.'}), 400
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.', 'details': str(e)}), 500

@product_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    """
    Create a new product.

    Request Body:
        name (str): The name of the product.
        price (float): The price of the product.

    Returns:
        Response: A JSON response containing the created product.
    """
    try:
        data = request.json
        if not data or not data.get('name') or not isinstance(data.get('price'), (int, float)):
            return jsonify({'error': 'Invalid input. "name" and "price" are required.'}), 400

        if data['price'] <= 0:
            return jsonify({'error': 'Price must be a positive value.'}), 400

        new_product = Product(name=data['name'], price=data['price'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred.', 'details': str(e)}), 500
