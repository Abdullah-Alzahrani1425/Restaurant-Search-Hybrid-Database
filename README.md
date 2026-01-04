# Hybrid Database Web Application: Restaurant Search System

[cite_start]A robust full-stack web application developed as a final project for **CCDS-222 Database II** at the **University of Jeddah**[cite: 67, 72]. [cite_start]This project demonstrates the integration of **Relational (SQL)** and **Non-Relational (NoSQL)** databases within a single server-client framework[cite: 88, 89].

## 🚀 Key Features
- [cite_start]**Secure Authentication:** User registration and login system powered by **MySQL** with password hashing using **bcrypt**[cite: 91, 106].
- [cite_start]**Advanced Search:** Dynamic restaurant search functionality utilizing **MongoDB** with regular expression queries[cite: 91, 105].
- [cite_start]**Hybrid Backend:** Dual database connectivity (MySQL for structured user data and MongoDB for flexible restaurant documents).
- [cite_start]**Responsive Feedback:** Real-time error handling and flash notifications for login/registration failures[cite: 109, 126].

## 🛠️ Tech Stack
- [cite_start]**Backend:** Python (Flask) [cite: 124]
- [cite_start]**Databases:** - MySQL (User Management) [cite: 93]
  - [cite_start]MongoDB (Restaurant Data) [cite: 96]
- [cite_start]**Security:** Bcrypt (Password Hashing) [cite: 110]
- [cite_start]**Frontend:** HTML/Jinaja2 (Server-side rendering) [cite: 94, 97]

## 🏗️ Architecture
The system follows a server-client model where the Flask backend acts as a bridge:
1. [cite_start]**User Auth:** Flask ↔ MySQL Connector ↔ `users` table[cite: 95].
2. [cite_start]**Search Logic:** Flask ↔ PyMongo ↔ `restaurant` collection[cite: 98].

## 👥 Contributors
- [cite_start]**Abdullah Alzahrani:** Backend Management & Auth Security[cite: 123].
- [cite_start]**Mohannad Alamri:** Documentation & Flask Routing[cite: 124].
- [cite_start]**Faisal Alotaibi:** MongoDB Setup & Query Logic[cite: 125].
- [cite_start]**Naif Alessa:** Frontend Results Display & Testing[cite: 126].

*Developed under the supervision of **Dr. [cite_start]Tariq Mohammed Alsahfi**[cite: 82].*
