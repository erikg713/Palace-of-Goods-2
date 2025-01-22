import React, { useState } from "react";
import axios from "../services/api";

const AdminDashboard = () => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");

  const handleCreateProduct = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("token");
      await axios.post(
        "/products",
        { name, description, price },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      alert("Product created successfully!");
    } catch (error) {
      alert("Product creation failed.");
    }
  };

  return (
    <form onSubmit={handleCreateProduct}>
      <h2>Create Product</h2>
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="text"
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <input
        type="number"
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />
      <button type="submit">Create</button>
    </form>
  );
};

export default AdminDashboard;
