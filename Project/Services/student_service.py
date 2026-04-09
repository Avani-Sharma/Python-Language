class Service:
    # get admission of student

    # update student information

    # inquiry about student

    # 1. get admission of student
    def add_student(self, student_id, name, age, course, email):
        if student_id in self.db.students:
            print("Student already exists!")
        else:
            student = Student(student_id, name, age, course, email)
            self.db.students[student_id] = student
            print("Student added successfully!")

    # 2. View all students
    def view_students(self):
        if not self.db.students:
            print("No students found!")
        else:
            for student in self.db.students.values():
                print(student.display())

    # 3. Search student
    def search_student(self, student_id):
        student = self.db.students.get(student_id)
        if student:
            print(student.display())
        else:
            print("Student not found!")

    # 4. Update student
    def update_student(self, student_id, name=None, age=None, course=None):
        student = self.db.students.get(student_id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if course:
                student.course = course
            print("Student updated successfully!")
        else:
            print("Student not found!")

    # 5. Delete student
    def delete_student(self, student_id):
        if student_id in self.db.students:
            del self.db.students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found!")