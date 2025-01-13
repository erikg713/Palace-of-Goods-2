// src/pages/Items.js
import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../context/AuthContext";

const Items = () => {
  const { token } = useContext(AuthContext);
  const [items, setItems] = useState([]);
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    try {
      const response = await fetch("/api/items", {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await response.json();
      setItems(data);
    } catch (error) {
      console.error("Failed to fetch items:", error);
    }
  };

  const handleAddItem = async () => {
    try {
      const response = await fetch("/api/items", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, price }),
      });
      if (response.ok) {
        fetchItems();
        setName("");
        setPrice("");
      }
    } catch (error) {
      console.error("Failed to add item:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-4">Items</h1>
      <div className="bg-white shadow-md rounded p-4 mb-4">
        <h2 className="text-xl font-bold mb-4">Add New Item</h2>
        <input
          type="text"
          placeholder="Item Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="shadow border rounded w-full py-2 px-3 mb-2"
        />
        <input
          type="number"
          placeholder="Price"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          className="shadow border rounded w-full py-2 px-3 mb-2"
        />
        <button
          onClick={handleAddItem}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Add Item
        </button>
      </div>
      <h2 className="text-xl font-bold mb-4">Your Items</h2>
      <ul>
        {items.map((item) => (
          <li key={item.id} className="bg-white shadow-md rounded p-4 mb-2">
            <h3 className="font-bold">{item.name}</h3>
            <p>Price: ${item.price}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Items;