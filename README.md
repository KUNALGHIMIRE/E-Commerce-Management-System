**TechStore - Full-Stack E-Commerce Application**

A scalable full-stack e-commerce web application that allows users to browse products, manage a shopping cart, and complete checkout. Built using a 3-tier architecture with React, Flask, and PostgreSQL.

**Live Demo**
👉 https://e-commerce-management-system-10.onrender.com/

**System Overview**
Architecture Diagram
<img width="298" height="176" alt="image" src="https://github.com/user-attachments/assets/0a7b7ec7-34ff-4f52-b421-b6b21e1d1b17" />

**System Flow**
```
1.User interacts with React frontend
2.Frontend sends REST API requests to Flask backend
3.Flask processes business logic
4.PostgreSQL retrieves/stores product, cart, and order data
5.Backend returns JSON response
6.Frontend updates UI dynamically
```
**System Design**
```
The system follows a 3-tier architecture:

1️⃣ Presentation Layer (Frontend)
Built with React.js
Handles UI rendering and user interaction
Communicates with backend via REST APIs

2️⃣ Application Layer (Backend)
Built using Flask (Python)
Handles authentication logic, cart management, and order processing
Exposes RESTful API endpoints

3️⃣ Data Layer (Database)
PostgreSQL database
Stores:
Users
Products
Cart items
Orders
```

**API Communication**
```
REST API-based architecture
JSON used for request/response
Stateless backend design
```
**Features**

User Features
```
1.Browse products with images
2.ategory filtering (Electronics, Fashion, etc.)
3.Search products
4.Add to cart with quantity control
5.Remove/update cart items
6.Checkout system with order confirmation
```
**System Features**
```
1.Session-based cart persistence
2.RESTful API architecture
3.Modular backend structure
4.Database-driven product & order management
5.Scalable 3-tier architecture
```
**Tech Stack**
```
1.Frontend: React.js, HTML5, CSS3
2.Backend: Flask (Python)
3.Database: PostgreSQL
4.Deployment: Render
```

**Database Schema**
```
Users → (id, name, email, password)
Products → (id, name, price, category, image)
Cart → (id, user_id, product_id, quantity)
Orders → (id, user_id, total_price, status)
```
**Key Design Highlights**
```
3-tier scalable architecture (Frontend → Backend → Database)
REST API communication using JSON
Session-based cart management
Modular and maintainable backend design
Production deployment using Render
```
