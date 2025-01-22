import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///palace_of_goods.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    PI_API_KEY = os.getenv("PI_API_KEY")
