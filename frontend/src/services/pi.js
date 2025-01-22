// src/services/pi.js

import { Pi } from "@pinetwork-js/sdk";

Pi.init({
  version: "2.0",
  sandbox: true, // Set to false for production
});

export const processPayment = async (paymentDetails) => {
  const { amount, memo, metadata } = paymentDetails;

  try {
    const payment = await Pi.createPayment({
      amount: amount,
      memo: memo,
      metadata: metadata,
      onReadyForServerApproval: async (paymentId) => {
        await fetch(`/api/payments/approve`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ paymentId }),
        });
      },
      onReadyForServerCompletion: async (paymentId) => {
        await fetch(`/api/payments/complete`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ paymentId }),
        });
      },
    });
    return payment;
  } catch (error) {
    console.error("Payment error:", error);
    throw error;
  }
};
