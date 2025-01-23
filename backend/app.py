from flask import Flask
from routes.marketplace import marketplace_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(marketplace_bp, url_prefix='/api/marketplace')

if __name__ == '__main__':
    app.run(debug=True)
