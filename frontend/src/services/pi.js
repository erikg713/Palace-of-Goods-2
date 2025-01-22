// frontend/src/services/pi.js

import { Pi } from "@pinetwork-js/sdk";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

Pi.init({
  version: "2.0",
  sandbox: true, // Use "true" for testing and "false" for production
});

export const processPayment = async (paymentDetails) => {
  const { amount, memo, metadata } = paymentDetails;

  try {
    const payment = await Pi.createPayment({
      amount: amount,
      memo: memo,
      metadata: metadata,
      onReadyForServerApproval: async (paymentId) => {
        await fetch(`${API_URL}/api/payments/approve`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ paymentId }),
        });
      },
      onReadyForServerCompletion: async (paymentId) => {
        await fetch(`${API_URL}/api/payments/complete`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ paymentId }),
        });
      },
      onCancel: (paymentId) => {
        console.log(`Payment ${paymentId} was canceled.`);
      },
      onError: (error, paymentId) => {
        console.error(`Error with payment ${paymentId}:`, error);
      },
    });
    return payment;
  } catch (error) {
    console.error("Payment processing failed:", error);
    throw error;
  }
};
