import React, { useState } from "react";

function LoginPage({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    if (email && password) {
      onLogin(email); // pass email to App
    } else {
      alert("Please enter email and password");
    }
  };

  const handleDemoLogin = () => {
    onLogin("demo@example.com");
  };

  return (
    <div className="login-page">
      <h1>Welcome to TechStore</h1>
      <p>Sign in to continue shopping</p>
      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email Address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <div className="options">
          <label>
            <input type="checkbox" /> Remember me
          </label>
          <a href="#">Forgot password?</a>
        </div>
        <button type="submit" className="sign-in-btn">Sign In</button>
        <button type="button" className="demo-btn" onClick={handleDemoLogin}>
          Continue with Demo Account
        </button>
      </form>
      <p>Don't have an account? <a href="#">Sign Up</a></p>
      <p className="terms">
        By continuing, you agree to our <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>
      </p>
    </div>
  );
}

export default LoginPage;
