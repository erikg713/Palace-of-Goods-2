import React, { useState } from "react";
import axios from "axios";

const Checkout = () => {
  const [status, setStatus] = useState("");

  const handleCheckout = () => {
    const totalAmount = 30;  // Example total amount
    const txid = "tx123";   // Example transaction ID

    axios.post("http://localhost:5000/api/complete-payment/tx123", {
      txid,
      total_amount: totalAmount
    })
      .then(response => setStatus("Payment completed successfully!"))
      .catch(error => setStatus("Payment failed!"));
  };

  return (
    <div>
      <h1>Checkout</h1>
      <button onClick={handleCheckout}>Pay with Pi</button>
      <p>{status}</p>
    </div>
  );
};

export default Checkout;
