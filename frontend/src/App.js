import React, { useState, useEffect } from "react";
import { Pi } from "pi-sdk";
import axios from "axios";
import Web3 from "web3";

const App = () => {
  const [user, setUser] = useState(null);
  const [items, setItems] = useState([]);
  const [walletAddress, setWalletAddress] = useState("");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/items")
      .then((response) => setItems(response.data))
      .catch((error) => console.error("Error fetching items:", error));
  }, []);

  const authenticate = async () => {
    try {
      const pi = new Pi();
      const user = await pi.authenticate();
      setUser(user);
    } catch (error) {
      console.error("Authentication failed:", error);
    }
  };

  const connectWallet = async () => {
    if (window.ethereum) {
      const web3 = new Web3(window.ethereum);
      try {
        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts",
        });
        setWalletAddress(accounts[0]);
      } catch (error) {
        console.error("Wallet connection failed:", error);
      }
    } else {
      alert("Please install a Web3 wallet!");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      {!user ? (
        <button
          onClick={authenticate}
          style={{
            padding: "10px 20px",
            backgroundColor: "#6200EA",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          Sign in with Pi
        </button>
      ) : (
        <div>
          <h2>Welcome, {user.username}</h2>
          <h1>Pi Network Marketplace</h1>
          <button onClick={connectWallet}>Connect Wallet</button>
          {walletAddress && <p>Connected Wallet: {walletAddress}</p>}
          <ul>
            {items.map((item) => (
              <li key={item.id}>
                {item.name} - {item.price} Pi
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default App;
