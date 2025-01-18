import React, { useState } from 'react';
import axios from 'axios';

const ProductForm = () => {
    const [name, setName] = useState('');
    const [price, setPrice] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:5000/products', { name, price })
            .then(() => {
                setName('');
                setPrice('');
                alert('Product added!');
            })
            .catch(error => console.error(error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <input
                type="number"
                placeholder="Price"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
            />
            <button type="submit">Add Product</button>
        </form>
    );
};

export default ProductForm;
