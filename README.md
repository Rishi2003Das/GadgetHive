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

## Getting Started

- Clone the repo:
  <pre> ```git clone https://github.com/your-username/GadgetHive.git
  cd GadgetHive``` </pre>
- Set up a virtual environment (optional but recommended):
  <pre> ```python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate``` </pre>
- Install dependencies:
  <pre> ```pip install -r requirements.txt``` </pre>
-  Run the application:
    <pre> ```python run.py``` </pre>
