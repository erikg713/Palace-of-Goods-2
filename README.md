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

## Backend Setup ##
pip install -r requirements.txt
python run.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
