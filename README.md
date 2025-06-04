
<p align="center">
  <img src="https://github.com/bdbaraban/holbertonbnb/blob/master/assets/hbnb-logo.png?raw=true" alt="HBnB Logo" width="800"/>
</p>

<p align="center">
  <img src="https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif" alt="Coding with Redbull GIF" width="250"/><br>
  <b>Holberton + Redbull = HBnB powered!<br>
  Warning: This project was coded under the influence of way too much Redbull.<br>
  If you spot any bugs, blame the caffeine wings! 🪽😜</b>
</p>

<h1 align="center">🏠 HBnB Project</h1>

<p align="center">
  <b>Full-Stack Web Application developed at <a href="https://www.holbertonschool.com">Holberton School</a></b>
</p>

---

## 📚 Table of Contents

- [📌 Introduction](#-introduction)
- [🏗️ High-Level Architecture](#-high-level-architecture)
- [📘 Class Relationships](#-class-relationships)
- [🔁 Sequence Diagrams](#-sequence-diagrams)
- [👤 Author](#-author)

---

## 📌 Introduction

Welcome to the **HBnB** project!

This repository contains the architecture, technical documentation, and interaction diagrams for the HBnB web application—a clone of Airbnb—developed as part of the **Holberton School** curriculum.

> 🧱 **Tech Stack:** Python · Flask · SQLAlchemy · RESTful API · HTML/CSS · JS

---

## 🏗️ High-Level Architecture

### 📦 System Overview

![High-Level Package Diagram](part1/high_level_package.png)

#### 🧩 Layered Design

- **Presentation Layer**: Manages UI and API endpoints.
- **Business Logic Layer**: Core models and app logic (e.g., `User`, `Place`, `Review`, `Amenity`).
- **Persistence Layer**: Handles all database interactions.
- **Facade Pattern**: Acts as a bridge simplifying communications between layers.

---

## 📘 Class Relationships

### 🔗 Diagram Explanation

- **User → Place**: One-to-many ("owns").
- **Place → Review**: One-to-many ("has").
- **Place ↔ Amenity**: Many-to-many ("offers").

> 📌 Multiplicities such as `1`, `0..*` are shown on the relationship lines.

### 🖼️ UML Example

![Class Diagram](part1/class_diagram.png)

---

## 🔁 Sequence Diagrams

### 1️⃣ User Registration

![User Registration](part1/user_registration_sequence.png)

> Shows the flow from user input to database record creation and response.

---

### 2️⃣ Place Creation

![Place Creation](part1/place_creation.png)

> Describes how a user creates a new place listing with proper data handling.

---

### 3️⃣ Review Submission

![Review Submission](part1/review_submission.png)

> Displays how users submit and store reviews tied to specific places.

---

### 4️⃣ Fetching Places

![Fetching List of Places](part1/fetching_list_places.png)

> Illustrates how available places are queried and returned to the user.

---

## 👤 Author

- GitHub: [MINS2405](https://github.com/MINS2405/holbertonschool-hbnb)

---
## 🏆 I did HBnB all by myself!

No group, no secret help—just me, my keyboard, and a lot of coffee.  
Even Stack Overflow took a break and said, "You got this!" ☕😎

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" alt="Thank you GIF" width="300"/>
</p>


<p align="center">
  <b>© 2025 Holberton School – HBnB Project</b>
</p>


