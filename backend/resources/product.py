from flask_restful import Resource, reqparse
from models import db, Product

# Request parsers for input validation
product_parser = reqparse.RequestParser()
product_parser.add_argument("name", type=str, required=True, help="Name is required")
product_parser.add_argument("price", type=float, required=True, help="Price is required")

class ProductListResource(Resource):
    def get(self):
        """Retrieve all products."""
        products = Product.query.all()
        return [product.to_dict() for product in products], 200

    def post(self):
        """Create a new product."""
        args = product_parser.parse_args()
        product = Product(name=args["name"], price=args["price"])
        db.session.add(product)
        db.session.commit()
        return product.to_dict(), 201

class ProductResource(Resource):
    def get(self, product_id):
        """Retrieve a single product by ID."""
        product = Product.query.get_or_404(product_id)
        return product.to_dict(), 200

    def delete(self, product_id):
        """Delete a product."""
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted"}, 200
