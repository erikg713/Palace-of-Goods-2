import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const ProductDetail = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/product/${id}`)
      .then(response => setProduct(response.data))
      .catch(error => console.error("Error fetching product details:", error));
  }, [id]);

  return (
    <div>
      {product && (
        <>
          <h1>{product.name}</h1>
          <p>{product.description}</p>
          <p>Price: {product.price} Pi</p>
          <button>Add to Cart</button>
        </>
      )}
    </div>
  );
};

export default ProductDetail;
