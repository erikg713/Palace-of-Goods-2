// src/api/items.js
const API_URL = "/api/items";

export const getItems = async (token) => {
  const response = await fetch(API_URL, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.json();
};

export const addItem = async (item, token) => {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(item),
  });
  return response.json();
};