import axios from 'axios';

const API_URL = process.env.REACT_APP_BACKEND_URL;

export const getMarketplaceItems = async () => {
    const response = await axios.get(`${API_URL}/api/marketplace/items`);
    return response.data;
};

export const purchaseItem = async (itemId) => {
    const response = await axios.post(`${API_URL}/api/marketplace/purchase`, { itemId });
    return response.data;
};

export const fetchProducts = async () => {
  const response = await axios.get("/api/products");
  return response.data;
};
