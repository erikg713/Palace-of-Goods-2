// src/pages/Profile.js
import React, { useContext, useState } from "react";
import AuthContext from "../context/AuthContext";

const Profile = () => {
  const { user, token } = useContext(AuthContext);
  const [email, setEmail] = useState(user?.email || "");
  const [password, setPassword] = useState("");

  const handleUpdateProfile = async () => {
    try {
      const response = await fetch("/api/auth/profile", {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });
      if (response.ok) {
        alert("Profile updated successfully!");
      } else {
        alert("Failed to update profile.");
      }
    } catch (error) {
      console.error("Failed to update profile:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-4">Profile</h1>
      <div className="bg-white shadow-md rounded p-4">
        <h2 className="text-xl font-bold mb-4">Update Profile</h2>
        <input
          type="email"
          placeholder="Email"