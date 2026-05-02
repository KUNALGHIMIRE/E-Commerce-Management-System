// import React, { useState } from "react";
// import Navbar from "./components/Navbar";
// import Filter from "./components/Filter";
// import ProductCard from "./components/ProductCard";
// import ProductModal from "./components/ProductModal";
// import Cart from "./components/Cart";
// import LoginPage from "./components/LoginPage";
// import Checkout from "./components/Checkout";
// import OrderSuccess from "./components/OrderSuccess";
// import { products } from "./data/products";

// function App() {
//   const [isLoggedIn, setIsLoggedIn] = useState(false);
//   const [userEmail, setUserEmail] = useState("");
//   const [cart, setCart] = useState([]);
//   const [selectedProduct, setSelectedProduct] = useState(null);
//   const [category, setCategory] = useState("All");
//   const [step, setStep] = useState("shop");

//   const categories = ["All", ...new Set(products.map(p => p.category))];

//   const filteredProducts =
//     category === "All"
//       ? products
//       : products.filter(p => p.category === category);

//   const addToCart = (product) => {
//     setCart([...cart, product]);
//   };

//   const removeFromCart = (index) => {
//     setCart(cart.filter((_, i) => i !== index));
//   };

//   /* ---------- LOGIN ---------- */
//   if (!isLoggedIn) {
//     return (
//       <LoginPage
//         onLogin={(email) => {
//           setIsLoggedIn(true);
//           setUserEmail(email);
//         }}
//       />
//     );
//   }

//   /* ---------- CHECKOUT ---------- */
//   if (step === "checkout") {
//     return (
//       <Checkout
//         cart={cart}
//         onPay={() => {
//           setCart([]);
//           setStep("success");
//         }}
//         onBack={() => setStep("shop")}
//       />
//     );
//   }

//   /* ---------- ORDER SUCCESS ---------- */
//   if (step === "success") {
//     return <OrderSuccess onShopAgain={() => setStep("shop")} />;
//   }

//   /* ---------- SHOP ---------- */
//   return (
//     <div>
//       <Navbar cartCount={cart.length} userEmail={userEmail} />

//       <div className="container">
//         <Filter
//           categories={categories}
//           selectedCategory={category}
//           onSelectCategory={setCategory}
//         />

//         <div className="product-grid">
//           {filteredProducts.map(product => (
//             <ProductCard
//               key={product.id}
//               product={product}
//               onAddToCart={addToCart}
//               onViewDetails={setSelectedProduct}
//             />
//           ))}
//         </div>

//         <Cart
//           cartItems={cart}
//           onRemove={removeFromCart}
//           onCheckout={() => setStep("checkout")}
//         />

//         {selectedProduct && (
//           <ProductModal
//             product={selectedProduct}
//             onClose={() => setSelectedProduct(null)}
//           />
//         )}
//       </div>
//     </div>
//   );
// }

// export default App;
import React, { useState } from "react";
import Navbar from "./components/Navbar";
import Filter from "./components/Filter";
import ProductCard from "./components/ProductCard";
import ProductModal from "./components/ProductModal";
import Cart from "./components/Cart";
import LoginPage from "./components/LoginPage";
import Checkout from "./components/Checkout";
import OrderSuccess from "./components/OrderSuccess";
import { products } from "./data/products";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userEmail, setUserEmail] = useState("");
  const [cart, setCart] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [category, setCategory] = useState("All");
  const [step, setStep] = useState("shop");

  const categories = ["All", ...new Set(products.map(p => p.category))];

  const filteredProducts =
    category === "All"
      ? products
      : products.filter(p => p.category === category);

  // FIXED: Add to cart function
  const addToCart = async (product) => {
    try {
      const response = await fetch('http://localhost:5000/api/cart', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({
          id: product.id,
          name: product.name,
          price: product.price
        })
      });
      
      const result = await response.json();
      if (result.success) {
        const cartRes = await fetch('http://localhost:5000/api/cart', {
          credentials: 'include'
        });
        const newCart = await cartRes.json();
        setCart(newCart);
        alert(`${product.name} added to cart!`);
      }
    } catch (error) {
      console.error("Error:", error);
      // Fallback to local cart if backend fails
      setCart([...cart, product]);
      alert(`${product.name} added to cart!`);
    }
  };

  const removeFromCart = (index) => {
    setCart(cart.filter((_, i) => i !== index));
  };

  /* ---------- LOGIN ---------- */
  if (!isLoggedIn) {
    return (
      <LoginPage
        onLogin={(email) => {
          setIsLoggedIn(true);
          setUserEmail(email);
        }}
      />
    );
  }

  /* ---------- CHECKOUT ---------- */
  if (step === "checkout") {
    return (
      <Checkout
        cart={cart}
        onPay={() => {
          setCart([]);
          setStep("success");
        }}
        onBack={() => setStep("shop")}
      />
    );
  }

  /* ---------- ORDER SUCCESS ---------- */
  if (step === "success") {
    return <OrderSuccess onShopAgain={() => setStep("shop")} />;
  }

  /* ---------- SHOP ---------- */
  return (
    <div>
      <Navbar cartCount={cart.length} userEmail={userEmail} />

      <div className="container">
        <Filter
          categories={categories}
          selectedCategory={category}
          onSelectCategory={setCategory}
        />

        <div className="product-grid">
          {filteredProducts.map(product => (
            <ProductCard
              key={product.id}
              product={product}
              onAddToCart={addToCart}
              onViewDetails={setSelectedProduct}
            />
          ))}
        </div>

        <Cart
          cartItems={cart}
          onRemove={removeFromCart}
          onCheckout={() => setStep("checkout")}
        />

        {selectedProduct && (
          <ProductModal
            product={selectedProduct}
            onClose={() => setSelectedProduct(null)}
          />
        )}
      </div>
    </div>
  );
}

export default App;