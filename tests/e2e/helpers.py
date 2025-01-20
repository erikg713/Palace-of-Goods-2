# tests/e2e/helpers.py
import os
import requests

def setup_backend():
    """Prepare the backend for testing."""
    os.environ["FLASK_ENV"] = "testing"
    # Run other necessary setup actions

def seed_database(data):
    """Seed the database with test data."""
    url = os.getenv("DATABASE_SEED_URL", "http://localhost:5000/seed")
    response = requests.post(url, json=data)
    if response.status_code != 200:
        raise Exception(f"Failed to seed database: {response.text}")
