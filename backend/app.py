from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client['palaceofgoods']

# Sample route: Fetch products from MongoDB
@app.route('/api/mongo/products', methods=['GET'])
def get_mongo_products():
    products = list(mongo_db.products.find({}, {"_id": 0}))  # Exclude MongoDB `_id` field
    return jsonify(products)

# Add a product to MongoDB (admin functionality)
@app.route('/api/mongo/products', methods=['POST'])
def add_mongo_product():
    data = request.json
    mongo_db.products.insert_one(data)
    return jsonify({"message": "Product added successfully"}), 201

# Configure SQLite Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///palaceofgoods.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

sql_db = SQLAlchemy(app)
api = Api(app)

# Import and register resources
from resources.product import ProductResource, ProductListResource
api.add_resource(ProductListResource, "/api/sqlite/products")
api.add_resource(ProductResource, "/api/sqlite/products/<int:product_id>")

if __name__ == "__main__":
    sql_db.create_all()  # Create tables
    app.run(debug=True)
