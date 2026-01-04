# Hybrid Database System: Restaurant Search Application 🍔

This project is the final practical application for the **Database II (CCDS-222)** course at the **University of Jeddah**. It demonstrates the integration of both Relational (SQL) and Non-Relational (NoSQL) databases within a single web-based environment.

## 🛠️ Tech Stack
* **Backend:** Python using the Flask framework.
* **SQL Database:** MySQL for managing secure user authentication and registration.
* **NoSQL Database:** MongoDB for storing and querying flexible restaurant datasets.
* **Security:** Implemented password hashing using the `bcrypt` library.

## 🚀 Key Functionalities
* **User Management:** Secure Sign-up and Login system powered by MySQL.
* **Dynamic Search:** Advanced restaurant search engine allowing users to filter by Name, Borough, or Cuisine using MongoDB regular expressions.
* **Session Management:** Secure user sessions to handle access control between the login and search pages.
* **Error Handling:** Real-time feedback for incorrect login credentials or "no results found" scenarios.

## 📂 Project Structure
* `project_db.py`: The core backend logic and database connectors.
* `requirements.txt`: List of necessary libraries to run the application.
* `Project Report.pdf`: A comprehensive report detailing implementation steps, challenges, and learning outcomes.

---
**Supervised by:** Dr. Tariq Mohammed Alsahfi.
