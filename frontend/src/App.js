import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import ProductList from "./components/ProductList";
import ProductDetail from "./components/ProductDetail";
import Cart from "./components/Cart";
import Checkout from "./components/Checkout";
import AdminDashboard from "./components/AdminDashboard";
import Products from "./components/Products";

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

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<ProductList />} />
        <Route path="/product/:id" element={<ProductDetail />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/checkout" element={<Checkout />} />
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/admin/products" element={<Products />} />
      </Routes>
    </Router>
  );
};

export default App;
// Ensure the SDK is loaded before running this script
document.addEventListener('DOMContentLoaded', () => {
  // Pi SDK initialization
  const appId = 'your_app_id'; // Replace with your registered Pi app ID
  const authButton = document.getElementById('authButton');
  const balanceDisplay = document.getElementById('balance');

  // Initialize Pi SDK
  Pi.init({
    version: '2.0',
    sandbox: true, // Set to `false` for production
  });

  // Authenticate user on button click
  authButton.addEventListener('click', async () => {
    try {
      // Authenticate user
      const scopes = ['payments', 'username', 'wallet_address'];
      const user = await Pi.authenticate(scopes, appId);

      // Display a success message
      alert(`Welcome, ${user.username}! Fetching your balance...`);

      // Fetch the user's balance
      const balance = await fetchBalance(user.uid);
      balanceDisplay.textContent = `Your Pi balance: ${balance} Pi`;
    } catch (error) {
      console.error('Authentication failed:', error);
      alert('Authentication failed. Please try again.');
    }
  });

  // Function to fetch the user's balance
  async function fetchBalance(userId) {
    try {
      const response = await fetch(`https://api.minepi.com/v2/users/${userId}/balance`, {
        headers: {
          Authorization: `Bearer ${Pi.getAccessToken()}`,
        },
      });

      if (!response.ok) {
        throw new Error(`Error fetching balance: ${response.statusText}`);
      }

      const data = await response.json();
      return data.balance || 0;
    } catch (error) {
      console.error('Error fetching balance:', error);
      return 'Error retrieving balance';
    }
  }
});
