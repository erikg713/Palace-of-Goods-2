from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_talisman import Talisman
from config import config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_socketio import SocketIO
from backend.routes import routes_bp
app.register_blueprint(routes_bp, url_prefix='/api')
socketio = SocketIO()
from flask import Flask, request, jsonify
import operator

app = Flask(__name__)

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

@app.route('/calculate_totals', methods=['POST'])
def calculate_totals():
    data = request.json
    transactions = data.get("transactions", [])
    if not transactions:
        return jsonify({"error": "No transactions provided"}), 400
    
    running_totals = list(accumulate(transactions))
    return jsonify({"running_totals": running_totals}), 200

if __name__ == "__main__":
    app.run(debug=True)
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    socketio.init_app(app)
    # Other initializations...
    return app
limiter = Limiter(get_remote_address, app=None)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    limiter.init_app(app)
    # Other initializations...
    return app

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    Talisman(app, content_security_policy=None)

    # Register blueprints
    from routes.auth_routes import auth_bp
    from routes.item_routes import item_bp
    from routes.payment_routes import payment_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(item_bp, url_prefix='/api/items')
    app.register_blueprint(payment_bp, url_prefix='/api/payments')

    return app