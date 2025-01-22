# Palace of Goods - Backend

This is the backend for the **Palace of Goods** project, built with Flask. It provides RESTful APIs for managing products, user authentication, and integration with the Pi Network payment system.

---

## **Table of Contents**
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [Available Scripts](#available-scripts)
- [File Structure](#file-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## **Features**
- RESTful APIs for managing products.
- User authentication (registration, login, token-based sessions).
- Integration with the Pi Network payment system.
- Paginated API for product listing.
- Database migrations using Flask-Migrate.
- Secure password hashing and token generation.

---

## **Technologies Used**
- **Flask**: Web framework.
- **Flask-SQLAlchemy**: ORM for database interactions.
- **Flask-Migrate**: For database migrations.
- **Flask-CORS**: Enables cross-origin requests.
- **SQLite/PostgreSQL**: Database (use SQLite for local development).
- **PyJWT**: For JSON Web Token (JWT) authentication.
- **Python-Dotenv**: For managing environment variables.

---

## **Setup Instructions**

### Prerequisites
1. Install [Python 3.8+](https://www.python.org/downloads/).
2. Install [pip](https://pip.pypa.io/en/stable/).
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

Clone the Repository

git clone https://github.com/<your-username>/Palace-of-Goods.git
cd Palace-of-Goods/backend

Install Dependencies

pip install -r requirements.txt

Run the Application

python run.py

The backend will run at http://localhost:5000.


---

Environment Variables

Create a .env file in the backend/ directory with the following variables:

# Database configuration
DATABASE_URL=sqlite:///palace_of_goods.db  # Replace with your production database URL

# Application secret key
SECRET_KEY=your_secret_key

# Pi Network API key (for payments)
PI_API_KEY=your_pi_network_server_api_key


---

Available Scripts

Run the Application

python run.py

Run Database Migrations

1. Initialize migrations:

flask db init


2. Create a migration:

flask db migrate -m "Initial migration"


3. Apply migrations:

flask db upgrade



Run Tests

pytest


---

File Structure

backend/
├── app/
│   ├── __init__.py         # App factory and initialization
│   ├── routes.py           # API route definitions
│   ├── models.py           # Database models
│   ├── config.py           # Configuration settings
│   ├── db.py               # Database utilities
│   └── utils.py            # Helper functions
├── migrations/             # Database migrations (via Flask-Migrate)
├── tests/                  # Unit tests
│   ├── test_routes.py      # Tests for API routes
│   └── test_models.py      # Tests for models
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
├── run.py                  # Application entry point
└── README.md               # Documentation for backend


---

API Endpoints

Product Endpoints

GET /api/products: Fetch paginated list of products.

Query Parameters:

page: Page number (default: 1).

per_page: Items per page (default: 10).



POST /api/products: Add a new product.

Body:

{
  "name": "Product Name",
  "description": "Product Description",
  "price": 10.99
}



User Authentication Endpoints

POST /api/register: Register a new user.

Body:

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123"
}


POST /api/login: Log in a user.

Body:

{
  "email": "test@example.com",
  "password": "password123"
}



Payment Endpoints

POST /api/payments/approve: Approve a payment.

Body:

{
  "paymentId": "unique_payment_id"
}


POST /api/payments/complete: Complete a payment.

Body:

{
  "paymentId": "unique_payment_id"
}




---

Contributing

1. Fork the repository.


2. Create a feature branch:

git checkout -b feature-name


3. Commit your changes:

git commit -m "Add feature-name"


4. Push to the branch:

git push origin feature-name


5. Open a pull request.




---

License

This project is licensed under the MIT License. See the LICENSE file for details.

---

### **Steps to Use This Template**
1. Save this content as `README.md` in the `backend/` directory.
2. Replace placeholders like `<your-username>` and `your_secret_key` with actual values for your project.
3. Add additional details as necessary (e.g., new endpoints, features, or configurations).
