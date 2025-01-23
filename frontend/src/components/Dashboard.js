import React from "react";
import useAuth from "../hooks/useAuth";

const Dashboard = () => {
  const { user } = useAuth();

  return (
    <div>
      <h2>Welcome, {user?.username}!</h2>
      <p>This is your dashboard.</p>
    </div>
  );
};

export default Dashboard;
