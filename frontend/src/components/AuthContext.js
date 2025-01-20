import React, { createContext, useState, useContext } from "react";
import usePiAuth from "../hooks/usePiAuth";

// Create the AuthContext
const AuthContext = createContext();

// AuthProvider component
export const AuthProvider = ({ children }) => {
  const appId = "your_app_id"; // Replace with your actual Pi App ID
  const { user, balance, authenticateUser } = usePiAuth(appId);

  return (
    <AuthContext.Provider value={{ user, balance, authenticateUser }}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to use AuthContext
export const useAuth = () => {
  return useContext(AuthContext);
};
