// src/pages/Dashboard.js
import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

const Dashboard = () => {
  const { user } = useContext(AuthContext);

  return (
    <div>
      <h1>Welcome, {user?.username || "Guest"}!</h1>
      <p>Your personalized dashboard will appear here.</p>
    </div>
  );
};

export default Dashboard;