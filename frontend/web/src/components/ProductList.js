import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:5000/products')
            .then(response => {
                setProducts(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error(error);
                setError('Failed to fetch products.');
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <ul>
            {products.length > 0 ? (
                products.map(product => (
                    <li key={product.id}>
                        {product.name} - ${product.price}
                    </li>
                ))
            ) : (
                <p>No products available.</p>
            )}
        </ul>
    );
};

export default ProductList;
