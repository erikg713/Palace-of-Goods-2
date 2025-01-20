payment = Payment.query.filter_by(pi_payment_id='unique_payment_id').first()
if payment:
    payment.status = 'COMPLETED'  # Update status
    payment.completed_at = db.func.current_timestamp()  # Save completion timestamp
    db.session.commit()
<script src="https://sdk.minepi.com/pi-sdk.js"></script>// Initialize the Pi SDK
const appId = "your_app_id"; // Replace with your App ID
Pi.init({ app_id: appId, sandbox: true });

// Authenticate the user
document.getElementById("authButton").addEventListener("click", () => {
  Pi.authenticate(null, onIncompletePaymentFound).then(user => {
    console.log("Authenticated user:", user);

    // Retrieve and display the user's balance
    Pi.getBalance().then(balance => {
      console.log("User balance:", balance);
      document.getElementById("balance").innerText = `Your balance: ${balance.balance} Pi`;
    }).catch(error => {
      console.error("Error fetching balance:", error);
    });
  }).catch(error => {
    console.error("Authentication failed:", error);
  });
});

// Handle incomplete payments
function onIncompletePaymentFound(payment) {
  console.log("Incomplete payment found:", payment);
}// Initialize the Pi SDK
const appId = "your_app_id"; // Replace with your App ID
Pi.init({ app_id: appId, sandbox: true });

// Authenticate the user
document.getElementById("authButton").addEventListener("click", () => {
  Pi.authenticate(null, onIncompletePaymentFound).then(user => {
    console.log("Authenticated user:", user);

    // Retrieve and display the user's balance
    Pi.getBalance().then(balance => {
      console.log("User balance:", balance);
      document.getElementById("balance").innerText = `Your balance: ${balance.balance} Pi`;
    }).catch(error => {
      console.error("Error fetching balance:", error);
    });
  }).catch(error => {
    console.error("Authentication failed:", error);
  });
});

// Handle incomplete payments
function onIncompletePaymentFound(payment) {
  console.log("Incomplete payment found:", payment);
}// backend/src/index.ts

app.post("/incomplete", async (req, res) => {
  const payment = req.body.payment;
  const paymentId = payment.identifier;
  const txid = payment.transaction && payment.transaction.txid;
  const txURL = payment.transaction && payment.transaction._link;

  /* your custom logic checking against incomplete order in DB */
  const order = ...
  // ...

  /* check the transaction on the Pi blockchain */
  const horizonResponse = await axios.create({ timeout: 20000 }).get(txURL);
  const paymentIdOnBlock = horizonResponse.data.memo;

  /* check other data as well e.g. amount */
  if (paymentIdOnBlock !== order.pi_payment_id) {
    return res.status(400).json({ message: "Payment id doesn't match." });
  }

  /* mark the order as paid in your DB */
  // ...

  /* let Pi Servers know that the payment is completed */
  await axiosClient.post(`/v2/payments/${paymentId}/complete`, { txid }, config);
  return res.status(200).json({ message: `Handled the incomplete payment ${paymentId}` });
});// frontend/src/shop/index.ts

const signIn = async () => {
  const scopes = ["username", "payments"];
  const authResponse = await window.Pi.authenticate(scopes, onIncompletePaymentFound);

  /* pass obtained data to backend */
  await signInUser(authResponse);

  /* use the obtained data however you want */
  setUser(authResponse.user);
};

const signInUser = (authResult: any) => {
  axiosClient.post("/signin", { authResult }, config);

  return setShowModal(false);
};  // backend/src/index.ts

  app.post('/signin', async (req, res) => {
    try {
      /* verify with the user's access token */
      const me = await axiosClient.get(`/v2/me`, { headers: { 'Authorization': `Bearer ${currentUser.accessToken}` } });
      console.log(me);
    }
    catch (err) {
      console.error(err);
      return res.status(401).json({error: "User not authorized"});
    }
    return res.status(200).json({ message: "User signed in" });
  }import express from 'express';
import axios from 'axios';

const app = express();
app.use(express.json());

app.post("/incomplete", async (req, res) => {
  try {
    const payment = req.body.payment;
    const paymentId = payment.identifier;
    const txid = payment.transaction && payment.transaction.txid;
    const txURL = payment.transaction && payment.transaction._link;

    // Your custom logic checking against incomplete order in DB
    const order = await getOrderFromDB(paymentId); // Example function to get order from DB

    // Check the transaction on the Pi blockchain
    const horizonResponse = await axios.create({ timeout: 20000 }).get(txURL);
    const paymentIdOnBlock = horizonResponse.data.memo;

    // Check other data as well e.g. amount
    if (paymentIdOnBlock !== order.pi_payment_id) {
      return res.status(400).json({ message: "Payment id doesn't match." });
    }

    // Mark the order as paid in your DB
    await markOrderAsPaid(order.id); // Example function to mark order as paid

    // Let Pi Servers know that the payment is completed
    await axios.post(`/v2/payments/${paymentId}/complete`, { txid }, { timeout: 10000 });
    return res.status(200).json({ message: `Handled the incomplete payment ${paymentId}` });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: "Internal server error" });
  }
});

app.post('/signin', async (req, res) => {
  try {
    // Verify with the user's access token
    const me = await axios.get(`/v2/me`, { headers: { 'Authorization': `Bearer ${req.body.accessToken}` } });
    console.log(me.data);
    return res.status(200).json({ message: "User signed in" });
  } catch (err) {
    console.error(err);
    return res.status(401).json({ error: "User not authorized" });
  }
});

const getOrderFromDB = async (paymentId) => {
  // Implement this function to get the order from the database
};

const markOrderAsPaid = async (orderId) => {
  // Implement this function to mark the order as paid in the database
};

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import ProductList from "./components/ProductList";
import ProductDetail from "./components/ProductDetail";
import Cart from "./components/Cart";
import Checkout from "./components/Checkout";

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<ProductList />} />
        <Route path="/product/:id" element={<ProductDetail />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/checkout" element={<Checkout />} />
      </Routes>
    </Router>
  );
};

export default App;import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/cart">Cart</Link></li>
        <li><Link to="/checkout">Checkout</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Mock Database for Products and Orders
products = [
    {"id": 1, "name": "Product 1", "price": 10.0, "description": "Description for Product 1"},
    {"id": 2, "name": "Product 2", "price": 20.0, "description": "Description for Product 2"},
    {"id": 3, "name": "Product 3", "price": 30.0, "description": "Description for Product 3"}
]

orders = []

# Pi Network API Key
PI_API_KEY = "your_pi_network_api_key"

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

@app.route('/api/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/complete-payment/<payment_id>', methods=['POST'])
def complete_payment(payment_id):
    data = request.json
    total_amount = data.get('total_amount')
    txid = data.get('txid')

    profit = total_amount * 0.10  # Calculate 10% profit
    orders.append({"txid": txid, "total_amount": total_amount, "profit": profit})

    # Send to Pi Network API
    headers = {'Authorization': f'Bearer {PI_API_KEY}'}
    response = requests.post(f"https://api.minepi.com/v2/payments/{payment_id}/complete", headers=headers, json={"txid": txid})

    if response.status_code == 200:
        return jsonify({"message": "Payment completed", "profit": profit}), 200
    return jsonify({"error": "Payment failed"}), 500

@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(debug=True)import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/products")
      .then(response => setProducts(response.data))
      .catch(error => console.error("Error fetching products:", error));
  }, []);

  return (
    <div>
      <h1>Products</h1>
      {products.map(product => (
        <div key={product.id}>
          <Link to={`/product/${product.id}`}>
            <h2>{product.name}</h2>
            <p>{product.price} Pi</p>
          </Link>
        </div>
      ))}
    </div>
  );
};

export default ProductList;
