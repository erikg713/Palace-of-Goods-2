// src/api/payments.js
<script src="https://sdk.minepi.com/pi-sdk.js"></script>
<script>
  // Initialize the Pi Network SDK
  const { init } = Pi;
  init({
    version: "2.0",
    onReady: async () => {
      console.log("Pi SDK Ready");
      
      // Authenticate user
      const user = await Pi.authenticate({
        scopes: ["username", "payments"],
        onIncompletePaymentFound: (payment) => {
          console.log("Incomplete payment found:", payment);
        },
      });

      console.log("Authenticated user:", user);
    },
  });

  // Function to process payments
  async function processPayment(amount, metadata) {
    try {
      const payment = await Pi.createPayment({
        amount: amount,
        memo: metadata.memo,
        metadata: metadata,
      });

      console.log("Payment processed:", payment);
    } catch (error) {
      console.error("Payment error:", error);
    }
  }

  // Example: Initiate a payment
  processPayment(10, { memo: "Purchase in Palace of Goods" });
</script>

const API_URL = "/api/payments";

export const createPayment = async (amount, memo, token) => {
  const response = await fetch(`${API_URL}/create`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ amount, memo }),
  });
  return response.json();
};

export const getPaymentHistory = async (token) => {
  const response = await fetch(`${API_URL}/history`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.json();
};