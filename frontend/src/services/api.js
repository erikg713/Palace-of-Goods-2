const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

export const fetchProducts = async (page = 1, perPage = 10) => {
  const response = await fetch(`${API_URL}/api/products?page=${page}&per_page=${perPage}`);
  if (!response.ok) {
    throw new Error("Failed to fetch products");
  }
  return await response.json();
};

export const addProduct = async (product) => {
  const response = await fetch(`${API_URL}/api/products`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(product),
  });
  if (!response.ok) {
    throw new Error("Failed to add product");
  }
  return await response.json();
};

export const registerUser = async (user) => {
  const response = await fetch(`${API_URL}/api/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  });
  if (!response.ok) {
    throw new Error("Registration failed");
  }
  return await response.json();
};

export const loginUser = async (credentials) => {
  const response = await fetch(`${API_URL}/api/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });
  if (!response.ok) {
    throw new Error("Login failed");
  }
  return await response.json();
};
