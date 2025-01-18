import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Products = () => {
    const [products, setProducts] = useState([]);
    const [form, setForm] = useState({ name: '', price: '', stock: '' });

    useEffect(() => {
        axios.get('http://localhost:5000/admin/products')
            .then(response => setProducts(response.data))
            .catch(err => console.error(err));
    }, []);

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:5000/admin/products', form)
            .then(() => {
                setForm({ name: '', price: '', stock: '' });
                axios.get('http://localhost:5000/admin/products')
                    .then(response => setProducts(response.data));
            });
    };

    return (
        <div>
            <h2>Manage Products</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Name"
                    value={form.name}
                    onChange={(e) => setForm({ ...form, name: e.target.value })}
                />
                <input
                    type="number"
                    placeholder="Price"
                    value={form.price}
                    onChange={(e) => setForm({ ...form, price: e.target.value })}
                />
                <input
                    type="number"
                    placeholder="Stock"
                    value={form.stock}
                    onChange={(e) => setForm({ ...form, stock: e.target.value })}
                />
                <button type="submit">Save Product</button>
            </form>
            <ul>
                {products.map(product => (
                    <li key={product.id}>{product.name} - ${product.price}</li>
                ))}
            </ul>
        </div>
    );
};

export default Products;
