import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        // Fetch items from Flask backend
        axios.get("http://127.0.0.1:5000/api/items")
            .then((response) => setItems(response.data))
            .catch((error) => console.error("Error fetching data:", error));
    }, []);

    return (
        <div>
            <h1>Palace of Goods</h1>
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