# 🎓 Student Management System

A simple command-line application built with Python to manage student records using a database backend.

---

## 📋 Features

- Add new student records
- View all existing student records
- Delete student records by ID
- Persistent storage via a database

---

## 🗂️ Project Structure

```
project/
│
├── main.py                  # Entry point — CLI menu and user interaction
├── Models/
│   └── student.py           # Student data model/class
└── Services/
    └── student_service.py   # Database service layer (CRUD operations)
```

---

## ⚙️ Prerequisites

- Python

> Depending on your database backend (e.g., SQLite, MySQL), you may need additional packages. Install them with:

```bash
pip install -r requirements.txt
```

---

## 🚀 Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```

2. **Run the application**

```bash
python main.py
```

---

## 🖥️ Usage

Once the application starts, you'll be presented with a menu:

```
1. Press 1 to add Student
2. Press 2 to View all the students.
3. Press 3 to update the student details.
4. Press 4 to exit.
```

### Option 1 — Add a Student
You will be prompted to enter:
- Student ID
- Name
- Age
- Course
- Email

### Option 2 — View All Students
Displays a list of all students currently stored in the database.

### Option 3 — Delete a Student
Enter the Student ID to remove that student's record from the database.

### Option 4 — Exit
Exits the application.

---

## 🧱 Data Model

The `Student` class (defined in `Models/student.py`) holds the following fields:

| Field    | Type   | Description              |
|----------|--------|--------------------------|
| `id`     | String | Unique student identifier |
| `name`   | String | Full name of the student |
| `age`    | int    | Age of the student       |
| `course` | String | Enrolled course/program  |
| `email`  | String | Student's email address  |

---

## 🛠️ Service Layer

The `Service` class (defined in `Services/student_service.py`) handles all database interactions:

| Method           | Description                        |
|------------------|------------------------------------|
| `create_table()` | Initializes the database table     |
| `add_student()`  | Inserts a new student record       |
| `view_student()` | Retrieves all student records      |
| `delete()`       | Deletes a student record by ID     |

---

## 📌 Notes

- The database table is automatically created on startup via `create_table()`.
- Student ID is taken as a string on input but the delete operation expects an integer ID — ensure consistency in your data model.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
