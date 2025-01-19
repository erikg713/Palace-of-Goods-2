// backend/src/index.ts

app.post("/incomplete", async (req, res) => {
  const payment = req.body.payment;
  const paymentId = payment.identifier;
  const txid = payment.transaction && payment.transaction.txid;
  const txURL = payment.transaction && payment.transaction._link;

  /* your custom logic checking against incomplete order in DB */
  const order = ...
  // ...

  /* check the transaction on the Pi blockchain */
  const horizonResponse = await axios.create({ timeout: 20000 }).get(txURL);
  const paymentIdOnBlock = horizonResponse.data.memo;

  /* check other data as well e.g. amount */
  if (paymentIdOnBlock !== order.pi_payment_id) {
    return res.status(400).json({ message: "Payment id doesn't match." });
  }

  /* mark the order as paid in your DB */
  // ...

  /* let Pi Servers know that the payment is completed */
  await axiosClient.post(`/v2/payments/${paymentId}/complete`, { txid }, config);
  return res.status(200).json({ message: `Handled the incomplete payment ${paymentId}` });
});
