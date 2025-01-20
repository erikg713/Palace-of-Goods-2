import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import ProductList from "./components/ProductList";
import ProductDetail from "./components/ProductDetail";
import Cart from "./components/Cart";
import Checkout from "./components/Checkout";
import AdminDashboard from "./components/AdminDashboard";
import Products from "./components/Products";
import usePiAuth from "./hooks/usePiAuth";

const App = () => {
  const appId = "your_app_id"; // Replace with your Pi Network App ID
  const { user, balance, authenticateUser } = usePiAuth(appId);

  return (
    <Router>
      <Navbar />
      <div style={{ padding: "20px" }}>
        <h1>Welcome to Palace of Goods</h1>
        {!user ? (
          <button onClick={authenticateUser}>Authenticate with Pi</button>
        ) : (
          <div>
            <p>Welcome, {user.username}!</p>
            <p>Your balance: {balance} Pi</p>
          </div>
        )}
      </div>
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
