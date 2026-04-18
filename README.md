# 📝 Eli Haimov's Flask Todo API

A robust RESTful API for managing tasks, built by **Eli Haimov**. This project utilizes **Python (Flask)** and **MongoDB**, focusing on clean code, structural integrity, and professional error handling to ensure server stability.

---

## 🚀 Features
- **Full CRUD Support**: Create, Read, Update, and Delete tasks.
- **Database Integration**: Powered by MongoDB for flexible data storage.
- **Advanced Error Management**: Uses a global error handler to prevent server crashes.
- **Safe ID Validation**: Automatically handles invalid MongoDB ObjectIDs without crashing.

---

## 🛠 Tech Stack
- **Developer**: Eli Haimov
- **Backend**: Python 3.x, Flask
- **Database**: MongoDB (via PyMongo)
- **Error Handling**: Werkzeug Exceptions / BSON Validation
- **Testing Tool**: Postman

---

## 🛣 API Endpoints

| Method | Endpoint | Description | Request Body (JSON) |
| :--- | :--- | :--- | :--- |
| **GET** | `/tasks` | Retrieve all tasks from the DB | None |
| **GET** | `/tasks/<id>` | Get a specific task by its ID | None |
| **POST** | `/tasks` | Create a new task | `{"title": "..."}` |
| **PUT** | `/tasks/<id>` | Update an existing task | `{"title": "..."}` |
| **DELETE** | `/tasks/<id>` | Remove a task from the DB | None |

---

## ⚠️ Error Handling Logic

The project implements a **Global Error Handling** strategy designed by Eli Haimov. Instead of returning standard HTML error pages, the API always responds with a clean JSON object.

### Edge Cases Covered:
1. **Invalid ID Format**: 
   - If an ID is provided that is not a valid 24-character hex string (e.g., sending only 2 characters), the system performs a `raise NotFound`.
   - **Response**: `404 Not Found`.
   - **Goal**: To prevent `bson.errors.InvalidId` from causing a 500 Internal Server Error.

2. **Resource Not Found**:
   - If the ID is valid but does not exist in the database.
   - **Response**: `404 Not Found`.

3. **General Server Errors**:
   - Any unexpected code exception is caught and returned as a `500 Internal Server Error` in JSON format.

---

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>