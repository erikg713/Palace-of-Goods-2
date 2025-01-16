from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['palaceofgoods']

# Sample route: Fetch products
@app.route('/api/products', methods=['GET'])
def get_products():
    products = list(db.products.find({}, {"_id": 0}))  # Exclude MongoDB `_id` field
    return jsonify(products)

# Add a product (admin functionality)
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    db.products.insert_one(data)
    return jsonify({"message": "Product added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend
api = Api(app)

# Configure SQLite Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///palaceofgoods.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Import and register resources
from resources.product import ProductResource, ProductListResource
api.add_resource(ProductListResource, "/api/products")
api.add_resource(ProductResource, "/api/products/<int:product_id>")

if __name__ == "__main__":
    db.create_all()  # Create tables
    app.run(debug=True)
