// src/pages/Payments.js
import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../context/AuthContext";

const Payments = () => {
  const { token } = useContext(AuthContext);
  const [payments, setPayments] = useState([]);
  const [amount, setAmount] = useState("");
  const [memo, setMemo] = useState("");

  useEffect(() => {
    fetchPayments();
  }, []);

  const fetchPayments = async () => {
    try {
      const response = await fetch("/api/payments/history", {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await response.json();
      setPayments(data);
    } catch (error) {
      console.error("Failed to fetch payments:", error);
    }
  };

  const handleCreatePayment = async () => {
    try {
      const response = await fetch("/api/payments/create", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ amount, memo }),
      });
      if (response.ok) {
        alert("Payment created successfully!");
        fetchPayments(); // Refresh payment history
        setAmount("");
        setMemo("");
      } else {
        alert("Failed to create payment.");
      }
    } catch (error) {
      console.error("Failed to create payment:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-4">Payments</h1>

      {/* Create Payment */}
      <div className="bg-white shadow-md rounded p-4 mb-4">
        <h2 className="text-xl font-bold mb-4">Create Payment</h2>
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          className="shadow border rounded w-full py-2 px-3 mb-2"
        />
        <input
          type="text"
          placeholder="Memo"
          value={memo}
          onChange={(e) => setMemo(e.target.value)}
          className="shadow border rounded w-full py-2 px-3 mb-2"
        />
        <button
          onClick={handleCreatePayment}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Create Payment
        </button>
      </div>

      {/* Payment History */}
      <h2 className="text-xl font-bold mb-4">Payment History</h2>
      <ul>
        {payments.map((payment) => (
          <li key={payment.payment_id} className="bg-white shadow-md rounded p-4 mb-2">
            <h3 className="font-bold">Payment ID: {payment.payment_id}</h3>
            <p>Status: {payment.status}</p>
            <p>Amount: ${payment.amount}</p>
            <p>Date: {new Date(payment.created_at).toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Payments;