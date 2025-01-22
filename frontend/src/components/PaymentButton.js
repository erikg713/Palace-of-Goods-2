import React from "react";
import axios from "../services/api";

const PaymentButton = ({ amount }) => {
  const handlePayment = async () => {
    try {
      const response = await axios.post("/payments/initiate", { amount });
      alert("Payment initiated successfully!");
    } catch (error) {
      alert("Payment failed.");
    }
  };

  return <button onClick={handlePayment}>Pay {amount} Pi</button>;
};

export default PaymentButton;
