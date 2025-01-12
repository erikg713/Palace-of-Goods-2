import React, { useState, useEffect } from "react";
import axios from "axios";
const updateItem = async (id, updatedItem) => {
    try {
        await axios.put(`http://127.0.0.1:5000/api/update-item/${id}`, updatedItem, {
            headers: { Authorization: `Bearer ${token}` },
        });
        fetchItems();
    } catch (err) {
        console.error("Failed to update item:", err.response.data);
    }
};

const deleteItem = async (id) => {
    try {
        await axios.delete(`http://127.0.0.1:5000/api/delete-item/${id}`, {
            headers: { Authorization: `Bearer ${token}` },
        });
        fetchItems();
    } catch (err) {
        console.error("Failed to delete item:", err.response.data);
    }
};
function App() {
    const [token, setToken] = useState(null);
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [items, setItems] = useState([]);
    const [newItem, setNewItem] = useState({ name: "", price: "" });

    const register = async (e) => {
        e.preventDefault();
        try {
            await axios.post("http://127.0.0.1:5000/api/register", { username, password });
            alert("User registered successfully! You can now log in.");
        } catch (err) {
            console.error("Registration failed:", err.response.data);
        }
    };

    const login = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:5000/api/login", { username, password });
            setToken(response.data.access_token);
            alert("Login successful!");
        } catch (err) {
            console.error("Login failed:", err.response.data);
        }
    };

    const fetchItems = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:5000/api/items", {
                headers: { Authorization: `Bearer ${token}` },
            });
            setItems(response.data);
        } catch (err) {
            console.error("Failed to fetch items:", err.response.data);
        }
    };

    const addItem = async (e) => {
        e.preventDefault();
        try {
            await axios.post(
                "http://127.0.0.1:5000/api/add-item",
                newItem,
                { headers: { Authorization: `Bearer ${token}` } }
            );
            setNewItem({ name: "", price: "" });
            fetchItems();
        } catch (err) {
            console.error("Failed to add item:", err.response.data);
        }
    };

    return (
        <div>
            <h1>Palace of Goods</h1>
            {!token ? (
                <>
                    <h2>Register</h2>
                    <form onSubmit={register}>
                        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
                        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                        <button type="submit">Register</button>
                    </form>
                    <h2>Login</h2>
                    <form onSubmit={login}>
                        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
                        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                        <button type="submit">Login</button>
                    </form>
                </>
            ) : (
                <>
                    <h2>Items</h2>
                    <button onClick={fetchItems}>Fetch Items</button>
                    <ul>
                        {items.map((item) => (
                            <li key={item.id}>{item.name} - ${item.price.toFixed(2)}</li>
                        ))}
                    </ul>
                    <h2>Add Item</h2>
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
                </>
            )}
        </div>
    );
}

export default App;
<ul>
    {items.map((item) => (
        <li key={item.id}>
            {item.name} - ${item.price.toFixed(2)}
            <button onClick={() => updateItem(item.id, { name: "Updated Name", price: item.price })}>
                Update
            </button>
            <button onClick={() => deleteItem(item.id)}>Delete</button>
        </li>
    ))}
</ul>