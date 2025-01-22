from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from app.routes import bp as api_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    return app
