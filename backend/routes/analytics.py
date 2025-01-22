from flask import Blueprint, jsonify
from models.models import Order

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route('/sales', methods=['GET'])
def get_sales_data():
    sales = db.session.query(Order.product_id, db.func.sum(Order.quantity)).group_by(Order.product_id).all()
    return jsonify([
        {"product_id": sale[0], "total_sold": sale[1]}
        for sale in sales
    ])
