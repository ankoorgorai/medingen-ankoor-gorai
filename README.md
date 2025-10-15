# Medingen - Online Product & Review Platform

Medingen is a full-stack web application that allows users to browse products, view reviews, and interact with the platform.  
The backend is built with **Flask** and **MySQL**, and the frontend is developed using **React**.  

This project was completed as part of an interview assignment to demonstrate full-stack development skills, modular code structure, and responsive design.

---

## Project Structure
medingen-ANKOOR-GORAI/
│
├── backend/ # Flask API backend
│ ├── app.py # Main Flask application
│ ├── config.py # Configuration file (DB credentials, JWT secret)
│ ├── models.py # SQLAlchemy models representing database tables
│ ├── routes/ # API endpoint files
│ │ ├── auth.py # JWT-based authentication routes
│ │ ├── products.py # Endpoints for products, salt content, and descriptions
│ │ └── reviews.py # Endpoints for reviews
│ ├── requirements.txt # Python dependencies for Flask API
│ └── database.sql # MySQL database export with sample data
│
├── frontend/ # React frontend
│ ├── package.json # React project configuration and dependencies
│ ├── public/ # Static files (index.html, favicon, logo)
│ └── src/
│ ├── index.js # Entry point of React app
│ ├── App.js # Main App component
│ ├── components/ # Reusable React components
│ │ ├── Navbar.js
│ │ ├── ProductCard.js
│ │ ├── ReviewCard.js
│ │ └── LoginPrompt.js
│ ├── context/ # State management using React Context
│ │ └── AppContext.js
│ ├── services/ # API call functions
│ │ └── api.js
│ └── styles/ # CSS files for components
│ ├── App.css
│ ├── Navbar.css
│ ├── ProductCard.css
│ └── ReviewCard.css
│
└── README.md # Project documentation
