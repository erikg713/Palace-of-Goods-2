# Palace of Goods

**A Web3-powered marketplace leveraging the Pi Network ecosystem.**

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Project Directory Structure](#project-directory-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

Palace of Goods is a robust e-commerce platform designed for seamless shopping experiences. It offers:
- A user-friendly interface.
- Advanced search features.
- Secure payment options.
- Scalability and high performance for smooth shopping.

Explore our marketplace for a wide range of products with Web3 integration.

---

## Features
- **Dynamic Product Catalog**: Browse and filter thousands of items.
- **Secure Payment Gateway**: Multiple payment options (credit cards, PayPal, cryptocurrencies).
- **User Accounts**: Register, log in, and manage your profile.
- **Wishlist and Cart**: Save favorite items and manage your shopping cart.
- **Order Tracking**: Real-time updates on order statuses.
- **Admin Dashboard**: Control for sellers to manage products, categories, and orders.

---

## Tech Stack
- **Frontend**: React, Tailwind CSS
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Authentication**: JWT, OAuth
- **Deployment**: Vercel (frontend), Heroku (backend)

---

## Installation and Setup

### Prerequisites
- Node.js (v14 or higher)
- MongoDB (Local or MongoDB Atlas)

### Steps
#### Clone the Repository
```bash
git clone https://github.com/erikg713/Palace-of-Goods.git
cd Palace-of-Goods

pip install -r requirements.txt
python run.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Frontend Setup

1. Create and navigate to the frontend/ directory:

npx create-react-app frontend
cd frontend


2. Install dependencies:

npm install axios


3. Start the development server:

npm start

The app will run at http://localhost:3000.




---

Project Directory Structure

Palace-of-Goods/
├── backend/
│   ├── app.py               # Flask backend code
│   ├── requirements.txt     # Backend dependencies
│   └── venv/                # Virtual environment (optional)
├── frontend/
│   ├── src/
│   │   └── App.js           # Main React component
│   ├── public/
│   ├── package.json         # Frontend dependencies
│   └── build/               # Production build of React
└── README.md                # Project documentation


---

Contributing

We welcome contributions to enhance Palace of Goods. Please follow these steps:

1. Fork the repository.


2. Create a new branch:

git checkout -b feature-branch


3. Make your changes and commit:

git commit -m "Add new feature"


4. Push to your branch:

git push origin feature-branch


5. Submit a pull request.




---

PiOS License

