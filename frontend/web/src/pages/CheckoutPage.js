import React, { useState } from 'react';
import axios from 'axios';

const CheckoutPage = () => {
    const [cart, setCart] = useState([]);
    const [txId, setTxId] = useState('');

    const handleCheckout = async () => {
        try {
            const response = await axios.post('/orders', { products: cart });
            const paymentResponse = await axios.post('/payments', { tx_id: txId });
            alert('Payment Successful!');
        } catch (error) {
            console.error(error);
            alert('Payment Failed');
        }
    };

    return (
        <div>
            <h1>Checkout</h1>
            <button onClick={handleCheckout}>Pay with Pi</button>
        </div>
    );
};

export default CheckoutPage;
