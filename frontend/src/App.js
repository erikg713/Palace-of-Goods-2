import React, { useState } from "react";
import axios from "axios";

function App() {
    const [amount, setAmount] = useState("");
    const [paymentId, setPaymentId] = useState(null);

    const createPayment = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:5000/api/create-payment", {
                amount: parseFloat(amount),
                memo: "Payment for goods",
            }, {
                headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
            });
            setPaymentId(response.data.payment_id);
            alert("Payment created! Please confirm in the Pi app.");
        } catch (err) {
            console.error("Failed to create payment:", err.response.data);
        }
    };

    const completePayment = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:5000/api/complete-payment", {
                payment_id: paymentId,
            });
            alert("Payment completed successfully!");
            setPaymentId(null); // Reset after completion
        } catch (err) {
            console.error("Failed to complete payment:", err.response.data);
        }
    };

    return (
        <div>
            <h1>Palace of Goods</h1>
            <h2>Make a Payment</h2>
            <input
                type="number"
                placeholder="Enter amount"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
            />
            <button onClick={createPayment}>Create Payment</button>
            {paymentId && (
                <div>
                    <p>Payment ID: {paymentId}</p>
                    <button onClick={completePayment}>Complete Payment</button>
                </div>
            )}
        </div>
    );
}

export default App;
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
<nav className="navbar navbar-expand-lg navbar-light bg-light">
    <div className="container">
        <a className="navbar-brand" href="/">Palace of Goods</a>
        <div>
            <a className="nav-link" href="/login">Login</a>
            <a className="nav-link" href="/items">Items</a>
        </div>
    </div>
</nav>
function App() {
    return (
        <Router>
            <nav>
                <Link to="/">Home</Link>
                <Link to="/login">Login</Link>
                <Link to="/items">Items</Link>
            </nav>
            <Routes>
                <Route path="/" element={<h1>Welcome to Palace of Goods</h1>} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/items" element={<ItemsPage />} />
            </Routes>
        </Router>
    );
}

function LoginPage() {
    // Login logic here
    return <h2>Login Page</h2>;
}

function ItemsPage() {
    // Items logic here
    return <h2>Items Page</h2>;
}

export default App;
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
const logout = () => {
    setToken(null);
    setItems([]);
};

return (
    <div>
        {token ? <button onClick={logout}>Logout</button> : null}
        {/* Rest of your UI */}
    </div>
);
const [search, setSearch] = useState("");

const filteredItems = items.filter((item) =>
    item.name.toLowerCase().includes(search.toLowerCase())
);

return (
    <div>
        <input
            type="text"
            placeholder="Search items"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
        />
        <ul>
            {filteredItems.map((item) => (
                <li key={item.id}>
                    {item.name} - ${item.price.toFixed(2)}
                </li>
            ))}
        </ul>
    </div>
);