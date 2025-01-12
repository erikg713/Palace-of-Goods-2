import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
    const [items, setItems] = useState([]);
    const [newItem, setNewItem] = useState({ name: "", price: "" });

    // Fetch items from the backend
    useEffect(() => {
        axios.get("http://127.0.0.1:5000/api/items")
            .then((response) => setItems(response.data))
            .catch((error) => console.error("Error fetching data:", error));
    }, []);

    // Handle form submission
    const addItem = (e) => {
        e.preventDefault();
        axios.post("http://127.0.0.1:5000/api/add-item", newItem)
            .then((response) => {
                setItems([...items, response.data]);
                setNewItem({ name: "", price: "" }); // Reset form
            })
            .catch((error) => console.error("Error adding item:", error));
    };

    return (
        <div>
            <h1>Palace of Goods</h1>
            <form onSubmit={addItem}>
                <input
                    type="text"
                    placeholder="Item Name"
                    value={newItem.name}
                    onChange={(e) => setNewItem({ ...newItem, name: e.target.value })}
                />
                <input
                    type="number"
                    placeholder="Price"
                    value={newItem.price}
                    onChange={(e) => setNewItem({ ...newItem, price: e.target.value })}
                />
                <button type="submit">Add Item</button>
            </form>
            <ul>
                {items.map((item) => (
                    <li key={item.id}>
                        {item.name} - ${item.price.toFixed(2)}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;