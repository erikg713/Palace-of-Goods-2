// src/components/Common/Header.js

import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';  // Importing CSS for styling

const Header = () => {
  return (
    <header className="header">
      <div className="logo">
        <Link to="/">Palace of Goods</Link>
      </div>
      <nav className="nav">
        <ul>
          <li><Link to="/products">Products</Link></li>
          <li><Link to="/cart">Cart</Link></li>
          <li><Link to="/profile">Profile</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
