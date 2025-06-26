







# 🏨 HBnB - Business Logic & API

## 👥 Team
- **Yassin Jaghmim**
- **Mina Sinani**

## 📚 Project Description

This project is **Part 2 of the HBnB application**, and focuses on implementing the **Business Logic Layer** and the **Presentation Layer (API)** using **Flask** and **Flask-RESTx**.

The goal is to build a solid, modular backend foundation for HBnB, allowing you to **create, read, and update core entities** (User, Place, Review, Amenity) through **RESTful API endpoints**.

> ⚠️ **Authentication (JWT, Roles)** and **database persistence with SQLAlchemy** will be implemented in Part 3.

---

## 📦 Project Architecture

part2/
├── api/ # Presentation Layer (Flask RESTx)
│ ├── init.py
│ ├── v1/
│ │ ├── init.py
│ │ ├── users.py
│ │ ├── places.py
│ │ ├── reviews.py
│ │ └── amenities.py
├── business/ # Business Logic Layer
│ ├── init.py
│ ├── user.py
│ ├── place.py
│ ├── amenity.py
│ └── review.py
├── repository/ # Persistence Layer (in-memory for now)
│ ├── init.py
│ └── storage.py
├── facade/ # Facade Layer to simplify communication
│ ├── init.py
│ └── service.py
├── tests/ # Unit & integration tests
│ └── ...
├── app.py # Flask application entry point
└── README.md

markdown
Copier
Modifier

---

## 🎯 Learning Objectives

- Structure a modular Python project using Flask
- Implement core business logic with object-oriented principles
- Build RESTful APIs using Flask-RESTx
- Manage relationships between entities (e.g., User ↔ Place, Place ↔ Amenity)
- Apply the Facade design pattern to simplify API-business logic communication
- Write and run both manual (cURL/Postman) and automated (unittest/pytest) tests

---

## ✅ Implemented Features

### 🧠 Business Logic
- Entities: `User`, `Place`, `Review`, `Amenity`
- Shared base attributes: `id`, `created_at`, `updated_at`
- Relationships:
  - One `User` owns multiple `Places`
  - `Place` has many `Amenities` (many-to-many)
  - `Review` belongs to a `User` and a `Place`

### 🧩 Facade Layer
- Centralized services to abstract business logic from the API
- Decouples route handling from business rule implementation

### 🌐 API Endpoints (via Flask-RESTx)
- `/api/v1/users/`
  - `POST`: Create a new user
  - `GET`: List all users
  - `GET <id>`: Retrieve a specific user (no password shown)
  - `PUT <id>`: Update user info (except password)
- `/api/v1/amenities/`
  - `POST`, `GET`, `PUT` for amenities
- `/api/v1/places/`
  - `POST`, `GET`, `PUT` for places, including owner and amenities
- `/api/v1/reviews/`
  - Full CRUD: `POST`, `GET`, `PUT`, `DELETE`
  - Reviews are linked to both a `User` and a `Place`

---

## 🧪 Testing & Validation

- Manual testing via **cURL** and **Swagger** (auto-generated with Flask-RESTx)
- Automated testing using **unittest** or **pytest**
- Input validation (e.g., required fields, valid latitude/longitude)
- Response formats and status codes aligned with REST best practices

---

## 📖 Resources Used

- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [Flask-RESTx Docs](https://flask-restx.readthedocs.io/en/latest/)
- [REST API Best Practices](https://restfulapi.net/)
- [Python Project Structure Guide](https://docs.python-guide.org/writing/structure/)
- [Facade Design Pattern (Python)](https://refactoring.guru/design-patterns/facade/python/example)

---

## 🚧 To Be Implemented in Part 3

- JWT Authentication and Role-Based Access Control
- SQLAlchemy integration (replace in-memory storage)
- User and place deletion support
- Deployment & production configuration

---

## 📁 Repository

GitHub: [holbertonschool-hbnb](https://github.com/holbertonschool-hbnb)  
Directory: `part2/`

---

## ✅ Progress Summary

| Task                         | Status |
|-----------------------------|--------|
| Project Setup               | ✅ Done |
| Core Business Logic         | ✅ Done |
| User Endpoints              | ✅ Done |
| Amenity Endpoints           | ✅ Done |
| Place Endpoints             | ✅ Done |
| Review Endpoints            | ✅ Done |
| Testing and Validation      | ✅ Done |

---

## 📬 Contact

For any questions or contributions, feel free to contact the team members.

---
