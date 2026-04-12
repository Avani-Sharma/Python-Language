🎓 Student Management System
A simple command-line application built with Python for managing student records using a database backend.

📁 Project Structure
StudentManagementSystem/
│
├── Models/
│   └── student.py          # Student data model
│
├── Services/
│   └── student_service.py  # Database service layer (CRUD operations)
│
└── main.py                 # Entry point / CLI interface

✨ Features

Add Student — Register a new student with ID, name, age, course, and email
View All Students — Display a list of all registered students
Delete Student — Remove a student record by ID
Persistent Storage — Data is stored in a database via the service layer


🚀 Getting Started
Prerequisites

Python 3.x

Installation
bashgit clone https://github.com/Avani-Sharma/Python-Language/tree/main/Project/Student_Management_System
cd student-management-system
Run the Application
bashpython main.py

🖥️ Usage
Once running, you'll see an interactive menu:
1. Press 1 to add Student
2. Press 2 to View all the students.
3. Press 3 to update the student details.
4. Press 4 to exit.
OptionAction1Add a new student (prompts for ID, name, age, course, email)2View all student records3Delete a student by ID4Exit the application

🗃️ Data Model
Each student record contains the following fields:
FieldTypeDescriptionidStringUnique student identifiernameStringFull name of the studentageIntegerAge of the studentcourseStringEnrolled courseemailStringStudent email address

🏗️ Architecture
The project follows a layered architecture:

Model Layer (Models/student.py) — Defines the Student class representing the data structure
Service Layer (Services/student_service.py) — Handles all database interactions (create table, add, view, delete)
Presentation Layer (main.py) — CLI interface that takes user input and calls the service layer


🤝 Contributing

Fork the repository
Create a feature branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add your feature')
Push to the branch (git push origin feature/your-feature)
Open a Pull Request


📄 License
This project is licensed under the MIT License.