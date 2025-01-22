import React from "react";
import { processPayment } from "../services/pi";

const ProductDetail = ({ product }) => {
  const handlePayment = async () => {
    try {
      const paymentDetails = {
        amount: product.price,
        memo: `Purchase of ${product.name}`,
        metadata: { productId: product.id },
      };
      const payment = await processPayment(paymentDetails);
      alert("Payment successful!");
      console.log("Payment details:", payment);
    } catch (error) {
      alert("Payment failed: " + error.message);
    }
  };

  return (
    <div>
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <p>${product.price}</p>
      <button onClick={handlePayment}>Pay with Pi</button>
    </div>
  );
};

export default ProductDetail;
