import React, { useEffect, useState } from "react";
import { fetchProducts } from "../services/api";

const Home = () => {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadProducts = async () => {
      try {
        const data = await fetchProducts();
        setProducts(data.products);
      } catch (err) {
        setError("Failed to load products. Please try again later.");
      } finally {
        setLoading(false);
      }
    };
    loadProducts();
  }, []);

  return (
    <div>
      <h2>Welcome to Palace of Goods</h2>
      <p>Explore our marketplace and find amazing products!</p>

      <section>
        <h3>Our Products</h3>
        {loading ? (
          <p>Loading products...</p>
        ) : error ? (
          <p style={{ color: "red" }}>{error}</p>
        ) : products.length > 0 ? (
          <ul>
            {products.map((product) => (
              <li key={product.id}>
                <h4>{product.name}</h4>
                <p>{product.description}</p>
                <p>Price: ${product.price.toFixed(2)}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p>No products available right now. Check back soon!</p>
        )}
      </section>
    </div>
  );
};

export default Home;
