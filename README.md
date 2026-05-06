# 🛒 TechStore - Full-Stack E-Commerce Application

A scalable full-stack e-commerce web application that allows users to browse products, manage a shopping cart, and complete checkout.

Built using a **3-tier architecture** with React, Flask, and PostgreSQL.

## 🚀 Live Demo
[https://e-commerce-management-system.vercel.app](https://e-commerce-management-system.vercel.app)

## 🧱 System Overview

### 📌 Architecture Diagram

<p align="center">
  <img src="https://github.com/user-attachments/assets/0a7b7ec7-34ff-4f52-b421-b6b21e1d1b17" width="500" />
</p>

## 🔄 System Flow

- User interacts with React frontend  
- Frontend sends REST API requests to Flask backend  
- Flask processes business logic  
- PostgreSQL retrieves/stores product, cart, and order data  
- Backend returns JSON response  
- Frontend updates UI dynamically

## 🏗️ System Design

The system is designed using a **3-tier architecture** to ensure scalability, modularity, and maintainability.

---

### 1️⃣ Presentation Layer (Frontend)
- React.js-based user interface  
- Responsible for rendering UI components and handling user interactions  
- Communicates with backend through RESTful APIs  

---

### 2️⃣ Application Layer (Backend)
- Flask (Python) backend server  
- Handles business logic such as authentication, cart operations, and order processing  
- Provides REST API endpoints for frontend communication  

---

### 3️⃣ Data Layer (Database)
- PostgreSQL relational database  
- Manages persistent storage for:
  - Users  
  - Products  
  - Cart items  
  - Orders

  ## 🧠 Engineering Decisions

Key architectural and design decisions made to ensure scalability and simplicity:

- Adopted a 3-tier architecture to clearly separate UI, business logic, and data layers for better scalability and maintainability  
- Used REST APIs to enable stateless, simple, and standardized communication between frontend and backend  
- Implemented session-based cart management to keep the system lightweight while avoiding complex authentication overhead for cart operations

## 🔌 API Communication

The application follows a **RESTful API architecture** for communication between frontend and backend.

- REST-based architecture for scalable communication  
- JSON format used for all request and response data  
- Stateless backend design to ensure scalability and simplicity  

## 🔌 API Endpoints

- GET /products → Fetch all products  
- POST /cart → Add item to cart  
- DELETE /cart/:id → Remove item from cart  
- POST /checkout → Create order

## ⭐ Features

- Browse products with images  
- Category filtering (Electronics, Fashion, etc.)  
- Search products  
- Add to cart with quantity control  
- Remove/update cart items  
- Checkout system with order confirmation  

## ⚙️ System Features

The system is designed with scalability and maintainability in mind:

- Session-based cart persistence for better user experience  
- RESTful API architecture for efficient communication  
- Modular backend structure for easy maintenance and scalability  
- Database-driven product and order management system  
- Scalable 3-tier architecture supporting future expansion  

## 🧰 Tech Stack

The application is built using a modern full-stack technology stack:

- **Frontend:** React.js, HTML5, CSS3 for responsive UI  
- **Backend:** Flask (Python) for API and business logic  
- **Database:** PostgreSQL for relational data management  
- **Deployment:** Render for hosting and production deployment  


## 🗄️ Database Schema

The database is designed using a relational structure to manage users, products, cart, and orders efficiently.

- **Users** → (id, name, email, password)  
  Stores user authentication and profile information  

- **Products** → (id, name, price, category, image)  
  Stores product catalog data  

- **Cart** → (id, user_id, product_id, quantity)  
  Manages user shopping cart items  

- **Orders** → (id, user_id, total_price, status)  
  Stores order history and transaction details  

## 🚀 Key Design Highlights

The project is designed with production-level engineering principles:

- 3-tier scalable architecture (Frontend → Backend → Database) ensuring separation of concerns  
- REST API communication using JSON for lightweight and efficient data exchange  
- Session-based cart management for persistent user experience  
- Modular and maintainable backend design for easy scalability and updates  
- Production deployment using Render for real-world hosting experience

## 🔐 Environment Variables

Create a `.env` file in the backend directory:

# Database Configuration
DB_HOST=your_supabase_host  
DB_PORT=5432  
DB_NAME=postgres  
DB_USER=postgres  
DB_PASSWORD=your_password  

# API Configuration

SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret


# Frontend Configuration

FRONTEND_URL=http://localhost:5173
