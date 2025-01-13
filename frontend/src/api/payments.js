// src/api/payments.js
const API_URL = "/api/payments";

export const createPayment = async (amount, memo, token) => {
  const response = await fetch(`${API_URL}/create`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ amount, memo }),
  });
  return response.json();
};

export const getPaymentHistory = async (token) => {
  const response = await fetch(`${API_URL}/history`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.json();
};