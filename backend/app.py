from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from pi_pysdk import Pi
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import config

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register Blueprints
    from routes.auth_routes import auth_bp
    from routes.item_routes import item_bp
    from routes.payment_routes import payment_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(item_bp, url_prefix='/api/items')
    app.register_blueprint(payment_bp, url_prefix='/api/payments')

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
app = Flask(__name__)

# Configure the Pi SDK
PI_API_KEY = "your_pi_api_key_here"  # Get this from the Pi Developer Console
pi = Pi(api_key=PI_API_KEY)

@app.route('/api/create-payment', methods=['POST'])
@jwt_required()
def create_payment():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    amount = data.get('amount')
    memo = data.get('memo', 'Payment for goods')
    metadata = {"user_id": current_user_id}

    if not amount or amount <= 0:
        return jsonify({"msg": "Invalid payment amount"}), 400

    # Create a payment request
    try:
        payment = pi.create_payment(
            amount=amount,
            memo=memo,
            metadata=metadata,
        )
        return jsonify({"payment_id": payment['identifier']}), 201
    except Exception as e:
        return jsonify({"msg": "Failed to create payment", "error": str(e)}), 500

@app.route('/api/complete-payment', methods=['POST'])
def complete_payment():
    data = request.get_json()
    payment_id = data.get('payment_id')

    if not payment_id:
        return jsonify({"msg": "Payment ID is required"}), 400

    # Verify and complete the payment
    try:
        payment = pi.complete_payment(payment_id)
        return jsonify({"msg": "Payment completed", "payment": payment}), 200
    except Exception as e:
        return jsonify({"msg": "Failed to complete payment", "error": str(e)}), 500
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///palace_of_goods.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this for production
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Routes
@app.route('/api/update-item/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    current_user_id = get_jwt_identity()
    data = request.get_json()
    item = Item.query.filter_by(id=item_id, user_id=current_user_id).first()

    if not item:
        return jsonify({"msg": "Item not found"}), 404

    item.name = data.get('name', item.name)
    item.price = data.get('price', item.price)
    db.session.commit()

    return jsonify({"msg": "Item updated successfully"}), 200

@app.route('/api/delete-item/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    current_user_id = get_jwt_identity()
    item = Item.query.filter_by(id=item_id, user_id=current_user_id).first()

    if not item:
        return jsonify({"msg": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"msg": "Item deleted successfully"}), 200
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200

@app.route('/api/items', methods=['GET'])
@jwt_required()
def get_items():
    current_user_id = get_jwt_identity()
    items = Item.query.filter_by(user_id=current_user_id).all()
    return jsonify([{"id": item.id, "name": item.name, "price": item.price} for item in items])

@app.route('/api/add-item', methods=['POST'])
@jwt_required()
def add_item():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    current_user_id = get_jwt_identity()

    if not name or not price:
        return jsonify({"msg": "Invalid input"}), 400

    new_item = Item(name=name, price=price, user_id=current_user_id)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"msg": "Item added successfully"}), 201

if __name__ == "__main__":
    db.create_all()  # Creates database tables
    app.run(debug=True)
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, completed, failed
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

# Store payment details in create-payment route
@app.route('/api/create-payment', methods=['POST'])
@jwt_required()
def create_payment():
    # Existing code...
    try:
        payment = pi.create_payment(
            amount=total_amount,
            memo=memo,
            metadata={"user_id": current_user_id, "item_ids": item_ids},
        )
        # Save payment details to the database
        new_payment = Payment(
            identifier=payment['identifier'],
            user_id=current_user_id,
            amount=total_amount,
        )
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"payment_id": payment['identifier']}), 201
    except Exception as e:
        return jsonify({"msg": "Failed to create payment", "error": str(e)}), 500

# Update payment status in the complete-payment route
@app.route('/api/complete-payment', methods=['POST'])
def complete_payment():
    # Existing code...
    try:
        payment = pi.complete_payment(payment_id)
        # Update payment status in the database
        db_payment = Payment.query.filter_by(identifier=payment_id).first()
        if db_payment:
            db_payment.status = "completed"
            db.session.commit()
        return jsonify({"msg": "Payment completed successfully"}), 200
    except Exception as e:
        return jsonify({"msg": "Failed to complete payment", "error": str(e)}), 500