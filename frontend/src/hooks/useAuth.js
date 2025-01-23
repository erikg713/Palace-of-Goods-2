import { useState, useEffect } from "react";
import axios from "../services/api";

// Custom hook for managing authentication
const useAuth = () => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [loading, setLoading] = useState(true);

  // Automatically fetch user details if a token exists
  useEffect(() => {
    if (token) {
      fetchUser();
    } else {
      setLoading(false);
    }
  }, [token]);

  // Fetch user profile using the token
  const fetchUser = async () => {
    try {
      const response = await axios.get("/auth/profile", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUser(response.data.user);
    } catch (error) {
      console.error("Error fetching user profile:", error);
      logout(); // Log out if token is invalid or expired
    } finally {
      setLoading(false);
    }
  };

  // Login function
  const login = async (username, password) => {
    try {
      const response = await axios.post("/auth/login", {
        username,
        password,
      });
      const accessToken = response.data.access_token;
      localStorage.setItem("token", accessToken);
      setToken(accessToken);
      await fetchUser(); // Fetch user details after login
      return { success: true };
    } catch (error) {
      console.error("Login error:", error);
      return { success: false, message: error.response?.data?.message || "Login failed" };
    }
  };

  // Logout function
  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
    setToken(null);
  };

  // Registration function
  const register = async (username, password) => {
    try {
      const response = await axios.post("/auth/register", {
        username,
        password,
      });
      return { success: true, message: response.data.message };
    } catch (error) {
      console.error("Registration error:", error);
      return { success: false, message: error.response?.data?.message || "Registration failed" };
    }
  };

  return {
    user,
    token,
    loading,
    login,
    logout,
    register,
    isAuthenticated: !!user,
  };
};

export default useAuth;
