**TechStore - Full-Stack E-Commerce Application**

A scalable full-stack e-commerce web application that allows users to browse products, manage a shopping cart, and complete checkout. Built using a 3-tier architecture with React, Flask, and PostgreSQL.

**Live Demo**
👉 https://e-commerce-management-system-10.onrender.com/

**System Overview**
Architecture Diagram
<img width="298" height="176" alt="image" src="https://github.com/user-attachments/assets/0a7b7ec7-34ff-4f52-b421-b6b21e1d1b17" />

**System Flow**
User interacts with React frontend

Frontend sends REST API requests to Flask backend

Flask processes business logic

PostgreSQL retrieves/stores product, cart, and order data

Backend returns JSON response

Frontend updates UI dynamically

**System Design**

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
```
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
🧑‍💻 User Features
Browse products with images

Category filtering (Electronics, Fashion, etc.)

Search products

Add to cart with quantity control

Remove/update cart items

Checkout system with order confirmation

⚙️ System Features
Session-based cart persistence

RESTful API architecture

Modular backend structure

Database-driven product & order management

Scalable 3-tier architecture

🧰 Tech Stack
Frontend: React.js, HTML5, CSS3

Backend: Flask (Python)

Database: PostgreSQL

Deployment: Render

🗄️ Database Schema
Users → (id, name, email, password)

Products → (id, name, price, category, image)

Cart → (id, user_id, product_id, quantity)

Orders → (id, user_id, total_price, status)

🚀 Key Design Highlights
3-tier scalable architecture (Frontend → Backend → Database)

REST API communication using JSON

Session-based cart management

Modular and maintainable backend design

Production deployment using Render
