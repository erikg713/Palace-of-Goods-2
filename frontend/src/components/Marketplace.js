import React, { useEffect, useState } from 'react';
import { getMarketplaceItems, purchaseItem } from '../services/api';

const Marketplace = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        const fetchItems = async () => {
            const data = await getMarketplaceItems();
            setItems(data);
        };
        fetchItems();
    }, []);

    const handlePurchase = async (id) => {
        try {
            const response = await purchaseItem(id);
            alert(response.message);
        } catch (error) {
            console.error("Purchase failed", error);
        }
    };

    return (
        <div>
            <h1>Marketplace</h1>
            <div className="items">
                {items.map(item => (
                    <div key={item.id} className="item-card">
                        <h2>{item.name}</h2>
                        <p>Price: {item.price} {item.currency}</p>
                        <button onClick={() => handlePurchase(item.id)}>Buy</button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Marketplace;
