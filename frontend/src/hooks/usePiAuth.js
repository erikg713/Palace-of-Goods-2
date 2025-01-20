import { useState } from "react";

const usePiAuth = (appId) => {
  const [user, setUser] = useState(null);
  const [balance, setBalance] = useState(null);

  // Initialize Pi SDK
  Pi.init({
    app_id: appId,
    sandbox: true, // Set to false for production
  });

  const authenticateUser = async () => {
    try {
      const scopes = ["payments", "username", "wallet_address"];
      const authenticatedUser = await Pi.authenticate(scopes, handleIncompletePayment);
      setUser(authenticatedUser);

      // Fetch balance
      const userBalance = await fetchBalance(authenticatedUser.uid);
      setBalance(userBalance);
    } catch (error) {
      console.error("Authentication failed:", error);
    }
  };

  const fetchBalance = async (userId) => {
    try {
      const response = await fetch(`https://api.minepi.com/v2/users/${userId}/balance`, {
        headers: {
          Authorization: `Bearer ${Pi.getAccessToken()}`,
        },
      });

      if (!response.ok) throw new Error("Error fetching balance");

      const data = await response.json();
      return data.balance || 0;
    } catch (error) {
      console.error("Error fetching balance:", error);
      return 0;
    }
  };

  const handleIncompletePayment = (payment) => {
    console.log("Incomplete payment found:", payment);
  };

  return {
    user,
    balance,
    authenticateUser,
  };
};

export default usePiAuth;
