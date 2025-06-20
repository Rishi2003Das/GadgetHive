# 📱 GadgetHive — Encrypted Electronic Gadget Marketplace 🛒

**GadgetHive** is a secure, Python-based web application built using the Flask framework. It serves as an open marketplace where users can **register**, **login**, **buy**, and **sell** electronic gadgets like smartphones, laptops, smartwatches, and more. With encryption and user authentication, it ensures a safe and interactive shopping experience.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Register and login securely with password hashing via Flask-Bcrypt.
  - Unique user sessions handled securely using Flask's session management.

- 🛍️ **Marketplace Functionality**
  - Users can list electronic items for sale with images, prices, and specifications.
  - Browse a marketplace with item listings from other users.
  - Interactive UI/UX for smooth navigation.

- 💳 **Item Purchase & Sale**
  - Purchase listed items and remove them from open listings.
  - Items include images, brand info, specs, and condition.

- 🎨 **Responsive UI**
  - Clean Bootstrap 4 integration with custom styling.
  - Particle.js animated background and hover cards for modern look.
  - User testimonials and detailed product catalogue with images.

- 🧱 **Tech Stack**
  - **Backend**: Python, Flask, Flask-Bcrypt, Flask-SQLAlchemy
  - **Frontend**: HTML5, CSS3, Bootstrap 4, JavaScript
  - **Database**: SQLite3

---

## 📁 Project Structure

FlaskMarket/
│
├── static/
│   ├── images/
│   └── styles/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── market.html
│
├── market/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── forms.py
│
├── run.py
└── README.md

## 🎯 Goal: Learn and implement backend architecture from first principles.
**🛠️ What I built:**

✅ Secure User Registration/Login System with encrypted passwords via Flask-Bcrypt

✅ Authentication & session management with built-in data checks

✅ A real-time marketplace: users can list, buy, and remove items

✅ Backend-controlled purchase system with transaction logic

✅ SQLite3 Database integrated using SQLAlchemy ORM

✅ Responsive frontend using Bootstrap 4 (UI kept minimal for backend focus)

**🔍 What I Learned:**

Building and managing a relational database schema

Creating secure authentication flows

Structuring backend routes with Flask Blueprints

Handling user input validation, flash messages, and data queries efficiently

Orchestrating backend logic with a smooth, functional frontend

**💡 All components** — from encryption to marketplace logic — work in sync to create a secure and intuitive platform. Every function you see is coded and connected by me, making this a complete backend-led full-stack build.
