import express from 'express';
import axios from 'axios';

const app = express();
app.use(express.json());

app.post("/incomplete", async (req, res) => {
  try {
    const payment = req.body.payment;
    const paymentId = payment.identifier;
    const txid = payment.transaction && payment.transaction.txid;
    const txURL = payment.transaction && payment.transaction._link;

    // Your custom logic checking against incomplete order in DB
    const order = await getOrderFromDB(paymentId); // Example function to get order from DB

    // Check the transaction on the Pi blockchain
    const horizonResponse = await axios.create({ timeout: 20000 }).get(txURL);
    const paymentIdOnBlock = horizonResponse.data.memo;

    // Check other data as well e.g. amount
    if (paymentIdOnBlock !== order.pi_payment_id) {
      return res.status(400).json({ message: "Payment id doesn't match." });
    }

    // Mark the order as paid in your DB
    await markOrderAsPaid(order.id); // Example function to mark order as paid

    // Let Pi Servers know that the payment is completed
    await axios.post(`/v2/payments/${paymentId}/complete`, { txid }, { timeout: 10000 });
    return res.status(200).json({ message: `Handled the incomplete payment ${paymentId}` });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: "Internal server error" });
  }
});

app.post('/signin', async (req, res) => {
  try {
    // Verify with the user's access token
    const me = await axios.get(`/v2/me`, { headers: { 'Authorization': `Bearer ${req.body.accessToken}` } });
    console.log(me.data);
    return res.status(200).json({ message: "User signed in" });
  } catch (err) {
    console.error(err);
    return res.status(401).json({ error: "User not authorized" });
  }
});

const getOrderFromDB = async (paymentId) => {
  // Implement this function to get the order from the database
};

const markOrderAsPaid = async (orderId) => {
  // Implement this function to mark the order as paid in the database
};

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
