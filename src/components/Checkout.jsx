function Checkout({ onPay }) {
  return (
    <div className="checkout">
      <h2>Payment Details</h2>

      <input type="text" placeholder="Card Number" />
      <input type="text" placeholder="Card Holder Name" />
      <input type="text" placeholder="Expiry Date (MM/YY)" />
      <input type="password" placeholder="CVV" />

      <button className="pay-btn" onClick={onPay}>
        Pay Now
      </button>
    </div>
  );
}

export default Checkout;
