import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Determine the environment and set debug mode accordingly
    env = os.getenv('FLASK_ENV', 'production')
    if env == 'development':
        app.debug = True
    else:
        app.debug = False

    @app.route('/')
    def hello():
        return "Hello, World!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()