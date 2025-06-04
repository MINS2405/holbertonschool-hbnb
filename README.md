 ![HBnB Logo](https://github.com/bdbaraban/holbertonbnb/blob/master/assets/hbnb-logo.png?raw=true)

# 🏠 **HBnB Project**

---

## 📑 Table of Contents

- [Introduction](#introduction)

- [High-Level Architecture](#high-level-architecture)

- [Class Relationships](#class-relationships)

- [Sequence Diagrams for API Calls](#sequence-diagrams-for-api-calls)

- [Author](#author)


---

## 🟢 Introduction

Welcome to the **HBnB** project!  
This repository contains the technical documentation, architecture diagrams, and sequence diagrams for the HBnB application, developed as part of the Holberton School curriculum.

The **HBnB project** is a full-stack web application that allows users to list, search, and review places.  
This documentation provides a comprehensive overview of the system’s architecture, main components, and API interaction flows.

---

## 🟦 High-Level Architecture

### 📦 High-Level Package Diagram

![High-Level Package Diagram](part1/high_level_package.png)

#### 📝 Explanations

- **Presentation Layer**: Manages user interaction and exposes APIs.
- **Business Logic Layer**: Contains the main business logic and core models (User, Place, Review, Amenity).
- **Persistence Layer**: Handles all data storage and retrieval operations.
- **Facade Pattern**: Provides a unified interface between the presentation and business logic layers, simplifying communication.

---

## 🟣 Class Relationships

- **User — Place**:  
  A `User` can own multiple `Place` objects (`1` to `0..*`). This is shown by the **"owns"** relationship.

- **Place — Review**:  
  A `Place` can have multiple `Review` objects (`1` to `0..*`). This is shown by the **"has"** relationship.

- **Place — Amenity**:  
  There is a many-to-many relationship between `Place` and `Amenity` (`0..*` to `0..*`). This is shown by the **"offers"** or **"includes"** relationship.

> **Note:**  
> Multiplicity (`1`, `0..*`, etc.) is indicated at each end of the relationship lines in the class diagram.  
> The name of the relationship is placed above or below the line.

### 🖼️ Class Diagram Example

![Class Diagram Example](part1/class_diagram.png)

---

## 🟠 Sequence Diagrams for API Calls

### 1️⃣ User Registration

![User Registration Sequence Diagram](part1/user_registration_sequence.png)

**Description:**  
Shows how a user registers for a new account. The request flows from the user to the API, then to the business logic, and finally to the database. The result is returned to the user.

---

### 2️⃣ Place Creation

![Place Creation Sequence Diagram](part1/place_creation.png)

**Description:**  
Illustrates the process when a user creates a new place listing. The request is validated and saved in the database, with the outcome sent back to the user.

---

### 3️⃣ Review Submission

![Review Submission Sequence Diagram](part1/review_submission.png)

**Description:**  
Represents the steps when a user submits a review for a place. The review is processed and stored in the database, and a response is returned to the user.

---

### 4️⃣ Fetching a List of Places

![Fetching Places Sequence Diagram](part1/fetching_list_places.png)

**Description:**  
Shows how a user requests a list of places. The business logic queries the database, collects the results, and sends them back to the user through the API.

---

## 👤 Author

- [MINS2405](https://github.com/MINS2405/holbertonschool-hbnb.git)

---

<p align="center">
  <b>© 2025 Holberton School – HBnB Project</b>
</p>
