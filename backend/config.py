import os
import warnings

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///palace_of_goods.db')
    if not os.getenv('DATABASE_URL'):
        warnings.warn("DATABASE_URL environment variable is not set. Using default SQLite database.")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
    if not os.getenv('JWT_SECRET_KEY'):
        warnings.warn("JWT_SECRET_KEY environment variable is not set. Using default secret key.")
    
    PI_API_KEY = os.getenv('PI_API_KEY', 'your-pi-api-key')
    if not os.getenv('PI_API_KEY'):
        warnings.warn("PI_API_KEY environment variable is not set. Using default PI API key.")
    PI_API_KEY = os.getenv('PI_API_KEY', 'your-pi-api-key')

config = Config()