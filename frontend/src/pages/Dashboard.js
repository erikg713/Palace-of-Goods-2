// src/pages/Dashboard.js
import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

const Dashboard = () => {
  const { user } = useContext(AuthContext);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-4">Welcome, {user?.username}!</h1>
      <div className="bg-white shadow-md rounded p-4">
        <p className="text-gray-700">
          This is your dashboard. Access your items, payments, and profile
          details here.
        </p>
      </div>
    </div>
  );
};

export default Dashboard;