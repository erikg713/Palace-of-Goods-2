import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        let isMounted = true; // flag to track component mounting

        const fetchProducts = async () => {
            try {
                const response = await axios.get(process.env.REACT_APP_API_URL + '/products');
                if (isMounted) {
                    setProducts(response.data);
                    setLoading(false);
                }
            } catch (error) {
                if (isMounted) {
                    console.error(error);
                    setError(error.message || 'Failed to fetch products.');
                    setLoading(false);
                }
            }
        };

        fetchProducts();

        return () => {
            isMounted = false; // cleanup flag on component unmount
        };
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
