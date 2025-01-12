# Palace of Goods

## Overview
**Palace of Goods** is a robust e-commerce platform designed for seamless shopping experiences. It offers a user-friendly interface, advanced search features, and secure payment options. Built for scalability, the platform caters to businesses of all sizes.

---

## Features
- **Dynamic Product Catalog**: Easily browse and filter thousands of items.
- **Secure Payment Gateway**: Supports multiple payment options like credit cards, PayPal, and cryptocurrencies.
- **User Accounts**: Register, log in, and manage your profile.
- **Wishlist and Cart**: Save your favorite items and manage your shopping cart.
- **Order Tracking**: Track your orders in real time.
- **Admin Dashboard**: Full control for sellers to manage products, categories, and orders.

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
- MongoDB (Local or cloud-based like MongoDB Atlas)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/palace-of-goods.git
   cd palace-of-goods

1. Create the Project Directory

First, create the main directory to house both the backend and frontend.

mkdir Palace-of-Goods
cd Palace-of-Goods


---

2. Set Up the Flask Backend

1. Create a backend/ folder for the Flask backend:

mkdir backend
cd backend


2. Create a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install Flask and dependencies:

pip install flask flask-cors


4. Create the required files:

Create app.py:

touch app.py

Create requirements.txt to track dependencies:

pip freeze > requirements.txt



5. Add basic Flask boilerplate code in app.py:

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow React frontend to make API requests during development

@app.route('/api/items', methods=['GET'])
def get_items():
    # Example data
    items = [
        {"id": 1, "name": "Golden Cup", "price": 19.99},
        {"id": 2, "name": "Silver Sword", "price": 34.99},
    ]
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)


6. Test the Flask app: Run the backend:

python app.py

Visit http://127.0.0.1:5000/api/items in your browser. You should see the JSON data.




---

3. Set Up the React Frontend

1. Go back to the project root and create a frontend/ folder:

cd ..
npx create-react-app frontend


2. Navigate into the frontend/ folder:

cd frontend


3. Install Axios for making API requests:

npm install axios


4. Start the React development server:

npm start

This will launch the React app at http://localhost:3000.




---

4. Modify React to Fetch Data From Flask

1. Open src/App.js in the frontend/ folder and replace its contents with:

import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:5000/api/items")
            .then(response => setItems(response.data))
            .catch(error => console.error("Error fetching data:", error));
    }, []);

    return (
        <div>
            <h1>Palace of Goods</h1>
            <ul>
                {items.map(item => (
                    <li key={item.id}>
                        {item.name} - ${item.price.toFixed(2)}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;


2. Save and restart the React development server (npm start).


3. Visit http://localhost:3000. You should see the items fetched from the Flask backend displayed.




---

5. Project Directory Structure

At this stage, your project should look like this:

Palace-of-Goods/
├── backend/
│   ├── app.py               # Flask backend code
│   ├── requirements.txt     # Backend Python dependencies
│   └── venv/                # Python virtual environment (optional)
│
├── frontend/
│   ├── src/
│   │   └── App.js           # Main React component
│   ├── public/
│   ├── package.json         # Frontend dependencies
│   └── build/               # Production build of React (after `npm run build`)
│
└── README.md                # Project documentation


---

6. Run Flask and React Together

For development:

Run the Flask backend:

cd backend
python app.py

Run the React frontend:

cd frontend
npm start


The Flask backend will run on http://127.0.0.1:5000, and the React frontend will run on http://localhost:3000