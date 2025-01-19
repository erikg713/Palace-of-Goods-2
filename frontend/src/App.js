import React from "react";
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

export default App;


import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AdminDashboard from './components/AdminDashboard';
import Products from './components/Products';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/admin" element={<AdminDashboard />} />
                <Route path="/admin/products" element={<Products />} />
            </Routes>
        </Router>
    );
}
// Initialize the Pi SDK
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
}
export default App;
