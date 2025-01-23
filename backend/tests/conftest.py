import pytest
from app import app, db
from models.models import User, Product

@pytest.fixture(scope="module")
def test_client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use in-memory SQLite
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.session.remove()
            db.drop_all()


@pytest.fixture(scope="module")
def init_database():
    # Add a sample user and product to the test database
    user = User(username="testuser", password="testpassword")
    product = Product(name="Test Product", description="A sample product", price=10.99)

    db.session.add(user)
    db.session.add(product)
    db.session.commit()

    return {"user": user, "product": product}
