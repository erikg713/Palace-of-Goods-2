// index.js
require('dotenv').config();
const express = require('express');
const { Pi } = require('@pinetwork-js/sdk');

const app = express();
const port = process.env.PORT || 3000;

// Initialize Pi Network SDK
Pi.init({
  appId: process.env.PI_APP_ID,
  privateKey: process.env.PI_PRIVATE_KEY,
});

// Set up middleware
app.use(express.json());

// Route for Pi Authentication
app.get('/auth', async (req, res) => {
  const scopes = ['username', 'payments'];
  try {
    const authResult = await Pi.authenticate(scopes);
    res.json(authResult);
  } catch (error) {
    res.status(500).send('Authentication failed');
  }
});

// Route for Pi Payments
app.post('/pay', async (req, res) => {
  const { amount, memo, metadata } = req.body;
  try {
    const payment = await Pi.createPayment({
      amount,
      memo,
      metadata,
    });
    res.json(payment);
  } catch (error) {
    res.status(500).send('Payment creation failed');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});