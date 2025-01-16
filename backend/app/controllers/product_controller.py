from flask import request, jsonify
from app.models.product_model import Product
from app import db

def add_product():
    data = request.get_json()
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201

def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    products = Product.query.paginate(page=page, per_page=per_page)

    return jsonify({
        'products': [{
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock
        } for product in products.items],
        'total': products.total,
        'pages': products.pages,
        'current_page': products.page
    }), 200
