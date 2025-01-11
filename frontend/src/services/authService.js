import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const loginUser = async (credentials) => {
  const response = await axios.post(`${API_BASE_URL}/auth/login`, credentials);
  return response.data;
};

export const registerUser = async (userData) => {
  const response = await axios.post(`${API_BASE_URL}/auth/register`, userData);
  return response.data;
};