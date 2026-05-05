# 🛍️ TechStore - Full-Stack E-Commerce Application

A full-stack e-commerce web application that allows users to browse products, manage a shopping cart, and complete checkout. Built with a scalable architecture using React, Flask, and PostgreSQL.

---

## 🔗 Live Demo
https://e-commerce-management-system-10.onrender.com/

---

# 🧠 System Overview

<img width="298" height="176" alt="image" src="https://github.com/user-attachments/assets/0a7b7ec7-34ff-4f52-b421-b6b21e1d1b17" />


**System Flow**
1. User browses products on React UI
2. React sends API request to Flask backend
3. Backend fetches product data from PostgreSQL
4. User adds products to cart (session-based)
5. Checkout creates order entry in database
6. Confirmation returned to frontend

## 🧠 System Design

The application follows a 3-tier architecture:

1. Presentation Layer → React frontend handles UI and user interaction
2. Application Layer → Flask REST API handles business logic
3. Data Layer → PostgreSQL stores users, products, cart, and orders

Communication happens via REST APIs using JSON format.

**Features**

User Features

Browse product catalog with images

Category filtering (Electronics, Fashion, etc.)

Product search functionality

Add to cart with quantity control

Remove/update cart items

Checkout system with order confirmation

**System Features**

Session-based cart persistence

RESTful API architecture

Modular backend structure

Database-driven product & order management

**Tech Stack**

Frontend: React.js, HTML5, CSS3

Backend: Flask (Python)

Database: PostgreSQL

Deployment: Render

**System Architecture**

[ React Frontend ]

        ↓
[ Flask REST API ]

        ↓
[ PostgreSQL Database ]

**Database Schema**

Users (id, name, email, password)

Products (id, name, price, category, image)

Cart (id, user_id, product_id, quantity)

Orders (id, user_id,)

