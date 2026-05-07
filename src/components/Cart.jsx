// function Cart({ cartItems, onCheckout }) {
//   const total = cartItems.reduce((sum, item) => sum + item.price, 0);

//   return (
//     <div className="cart">
//       <h2>Cart</h2>

//       {cartItems.length === 0 ? (
//         <p>No items in cart</p>
//       ) : (
//         <>
//           <ul>
//             {cartItems.map((item, index) => (
//               <li key={index}>
//                 {item.name} - ${item.price}
//               </li>
//             ))}
//           </ul>

//           <h3>Total: ${total.toFixed(2)}</h3>

//           <button className="checkout-btn" onClick={onCheckout}>
//             Proceed to Checkout
//           </button>
//         </>
//       )}
//     </div>
//   );
// }

// export default Cart;
// function Cart({ cartItems, onRemove, onUpdateQuantity, onCheckout }) {
//   // Debug: See what we're getting
//   console.log("Cart items received:", cartItems);
  
//   // Calculate total
//   const total = cartItems.reduce((sum, item) => {
//     const price = parseFloat(item.product_price) || 0;
//     const qty = parseInt(item.quantity) || 1;
//     return sum + (price * qty);
//   }, 0);

//   // Show empty cart message
//   if (!cartItems || cartItems.length === 0) {
//     return (
//       <div className="cart-card">
//         <h2>🛒 Your Cart</h2>
//         <div className="empty-cart">
//           <p>Your cart is empty</p>
//           <p className="empty-cart-hint">Add some products to get started!</p>
//         </div>
//       </div>
//     );
//   }

//   return (
//     <div className="cart-card">
//       <h2>🛒 Your Cart ({cartItems.length} items)</h2>
      
//       <div className="cart-items">
//         {cartItems.map((item) => {
//           // Get values safely
//           const productName = item.product_name || "Product";
//           const productPrice = parseFloat(item.product_price) || 0;
//           const quantity = parseInt(item.quantity) || 1;
//           const itemTotal = productPrice * quantity;
          
//           return (
//             <div key={item.id} className="cart-item">
//               <div className="cart-item-info">
//                 <div className="cart-item-name">{productName}</div>
//                 <div className="cart-item-price">${productPrice.toFixed(2)}</div>
//               </div>
              
//               <div className="cart-item-controls">
//                 <div className="quantity-control">
//                   <button 
//                     onClick={() => onUpdateQuantity(item.product_id, quantity - 1)}
//                     className="qty-btn"
//                   >
//                     -
//                   </button>
//                   <span className="qty-value">{quantity}</span>
//                   <button 
//                     onClick={() => onUpdateQuantity(item.product_id, quantity + 1)}
//                     className="qty-btn"
//                   >
//                     +
//                   </button>
//                 </div>
//                 <button 
//                   onClick={() => onRemove(item.product_id)}
//                   className="remove-item"
//                 >
//                   🗑️
//                 </button>
//               </div>
              
//               <div className="cart-item-total">
//                 ${itemTotal.toFixed(2)}
//               </div>
//             </div>
//           );
//         })}
//       </div>
      
//       <div className="cart-summary">
//         <div className="cart-total">
//           <span>Total:</span>
//           <strong>${total.toFixed(2)}</strong>
//         </div>
//         <button className="checkout-btn" onClick={onCheckout}>
//           Proceed to Checkout →
//         </button>
//       </div>
//     </div>
//   );
// }

// export default Cart;
function Cart({ cartItems, onRemove, onUpdateQuantity, onCheckout }) {
  // Debug
  console.log("Cart items received:", cartItems);

  // Calculate total safely
  const total = cartItems.reduce((sum, item) => {
    const price = parseFloat(item.product_price || item.price) || 0;
    const qty = parseInt(item.quantity) || 1;

    return sum + price * qty;
  }, 0);

  // Empty cart
  if (!cartItems || cartItems.length === 0) {
    return (
      <div className="cart-card">
        <h2>🛒 Your Cart</h2>

        <div className="empty-cart">
          <p>Your cart is empty</p>
          <p className="empty-cart-hint">
            Add some products to get started!
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="cart-card">
      <h2>🛒 Your Cart ({cartItems.length} items)</h2>

      <div className="cart-items">
        {cartItems.map((item) => {
          // Debug each item
          console.log("Cart item:", item);

          // Support multiple backend field names
          const productId = item.product_id || item.id;

          const productName =
            item.product_name ||
            item.name ||
            "Product";

          const productPrice =
            parseFloat(item.product_price || item.price) || 0;

          const quantity =
            parseInt(item.quantity) || 1;

          const itemTotal = productPrice * quantity;

          return (
            <div key={productId} className="cart-item">
              {/* Product Info */}
              <div className="cart-item-info">
                <div className="cart-item-name">
                  {productName}
                </div>

                <div className="cart-item-price">
                  ${productPrice.toFixed(2)}
                </div>
              </div>

              {/* Controls */}
              <div className="cart-item-controls">
                <div className="quantity-control">
                  <button
                    className="qty-btn"
                    onClick={() =>
                      onUpdateQuantity(
                        productId,
                        quantity - 1
                      )
                    }
                  >
                    -
                  </button>

                  <span className="qty-value">
                    {quantity}
                  </span>

                  <button
                    className="qty-btn"
                    onClick={() =>
                      onUpdateQuantity(
                        productId,
                        quantity + 1
                      )
                    }
                  >
                    +
                  </button>
                </div>

                <button
                  className="remove-item"
                  onClick={() => onRemove(productId)}
                >
                  🗑️
                </button>
              </div>

              {/* Item Total */}
              <div className="cart-item-total">
                ${itemTotal.toFixed(2)}
              </div>
            </div>
          );
        })}
      </div>

      {/* Summary */}
      <div className="cart-summary">
        <div className="cart-total">
          <span>Total:</span>
          <strong>${total.toFixed(2)}</strong>
        </div>

        <button
          className="checkout-btn"
          onClick={onCheckout}
        >
          Proceed to Checkout →
        </button>
      </div>
    </div>
  );
}

export default Cart;