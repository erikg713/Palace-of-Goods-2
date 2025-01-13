from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_socketio import SocketIO
import operator

# Initialize Flask extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()
limiter = Limiter(get_remote_address, app=None)
socketio = SocketIO()

# Function to calculate running totals
def accumulate(iterable, func=operator.add):
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total

# Flask app factory function
def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Load configuration from config.py

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)
    Talisman(app, content_security_policy=None)
    socketio.init_app(app)

    # Register blueprints
    from backend.routes.auth_routes import auth_bp
    from backend.routes.item_routes import item_bp
    from backend.routes.payment_routes import payment_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(item_bp, url_prefix='/api/items')
    app.register_blueprint(payment_bp, url_prefix='/api/payments')

    # Add a route for running totals
    @app.route('/api/calculate_totals', methods=['POST'])
    def calculate_totals():
        data = request.json
        transactions = data.get("transactions", [])
        if not transactions:
            return jsonify({"error": "No transactions provided"}), 400

        running_totals = list(accumulate(transactions))
        return jsonify({"running_totals": running_totals}), 200

    return app


# Run the app if executed directly
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)