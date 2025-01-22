const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

export const fetchProducts = async () => {
  const response = await fetch(`${API_URL}/api/products`);
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
