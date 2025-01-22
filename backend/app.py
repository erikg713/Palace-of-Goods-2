# app.py (Factory Pattern)

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import bcrypt
import jwt

db = SQLAlchemy()  # <-- Moved outside create_app so we can init_app()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure secret key for JWT
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

    # Database Config
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'palace_of_goods')
    DB_PORT = os.getenv('DB_PORT', '5432')

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Initialize db with the app

    #######################################
    # MODELS
    #######################################
    class User(db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password_hash = db.Column(db.String(128), nullable=False)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)

    class Product(db.Model):
        __tablename__ = 'products'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(120), nullable=False)
        price = db.Column(db.Float, nullable=False)
        description = db.Column(db.Text, nullable=True)
        seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)

    class Order(db.Model):
        __tablename__ = 'orders'
        id = db.Column(db.Integer, primary_key=True)
        product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
        buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        total_price = db.Column(db.Float, nullable=False)
        platform_fee = db.Column(db.Float, nullable=False)
        seller_earnings = db.Column(db.Float, nullable=False)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #######################################
    # UTILITIES
    #######################################
    def create_jwt_token(user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow()
        }
        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        return token

    def decode_jwt_token(token):
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            return payload
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return None

    def hash_password(plain_password):
        return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())

    def check_password(plain_password, hashed):
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed)

    #######################################
    # ROUTES
    #######################################
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "ok"}), 200

    @app.route('/register', methods=['POST'])
    def register():
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if not username or not email or not password:
            return jsonify({'message': 'Missing fields'}), 400

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400

        hashed_pw = hash_password(password)
        new_user = User(username=username, email=email, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        token = create_jwt_token(new_user.id)
        return jsonify({'message': 'User registered successfully', 'token': token}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'message': 'Invalid email or password'}), 401

        if not check_password(password, user.password_hash):
            return jsonify({'message': 'Invalid email or password'}), 401

        token = create_jwt_token(user.id)
        return jsonify({'message': 'Login successful', 'token': token}), 200

    @app.route('/products', methods=['GET'])
    def list_products():
        products = Product.query.all()
        product_list = []
        for p in products:
            product_list.append({
                'id': p.id,
                'name': p.name,
                'price': p.price,
                'description': p.description,
                'seller_id': p.seller_id
            })
        return jsonify(product_list), 200

    @app.route('/products', methods=['POST'])
    def create_product():
        token = request.headers.get('Authorization', None)
        if not token:
            return jsonify({'message': 'Authorization token missing'}), 401
        
        token_payload = decode_jwt_token(token)
        if not token_payload:
            return jsonify({'message': 'Invalid or expired token'}), 401

        user_id = token_payload.get('user_id')
        data = request.json
        name = data.get('name')
        price = data.get('price')
        description = data.get('description', '')

        new_product = Product(name=name, price=price, description=description, seller_id=user_id)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created', 'product_id': new_product.id}), 201

    @app.route('/purchase', methods=['POST'])
    def purchase_product():
        token = request.headers.get('Authorization', None)
        if not token:
            return jsonify({'message': 'Authorization token missing'}), 401
        
        token_payload = decode_jwt_token(token)
        if not token_payload:
            return jsonify({'message': 'Invalid or expired token'}), 401

        buyer_id = token_payload.get('user_id')
        data = request.json
        product_id = data.get('product_id')

        product = Product.query.get(product_id)
        if not product:
            return jsonify({'message': 'Product not found'}), 404

        total_price = product.price
        platform_fee = total_price * 0.10
        seller_earnings = total_price - platform_fee

        new_order = Order(
            product_id=product_id,
            buyer_id=buyer_id,
            total_price=total_price,
            platform_fee=platform_fee,
            seller_earnings=seller_earnings
        )
        db.session.add(new_order)
        db.session.commit()

        return jsonify({
            'message': 'Purchase successful (Mock)',
            'order_id': new_order.id,
            'total_price': total_price,
            'platform_fee': platform_fee,
            'seller_earnings': seller_earnings
        }), 200

    #######################################
    # CLI COMMANDS (if needed)
    #######################################
    @app.cli.command('create_db')
    def create_db():
        db.create_all()
        print("Database tables created.")

    return app
