// frontend/src/Shop/index.ts

const onIncompletePaymentFound = (payment: PaymentDTO) => {
  console.log("onIncompletePaymentFound", payment);
  return axiosClient.post("/incomplete", { payment }, config);
};

const signIn = async () => {
  // ...
  const authResponse = await window.Pi.authenticate(scopes, onIncompletePaymentFound);
  // ...
};
