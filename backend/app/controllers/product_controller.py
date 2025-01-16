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
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock
    } for product in products]), 200
