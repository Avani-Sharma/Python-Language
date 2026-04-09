import os 
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Database.connection import create_connection
from Models.student import Student
class Service:
    def create_table(self):
        conn = create_connection()
        # cursor :  pointer which is used to move into the database
        # which is used to execute the sql queries
        cursor = conn.cursor()
        # here we're executing the sql command using the python
        cursor.execute("""create table if not exists student(
                    id integer primary key autoincrement,
                    name text, 
                    age integer,
                    course text,
                    email text)
                """)
        conn.commit()
        conn.close()

    # insert one student into the table
    def add_student(self, student):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('insert into student (name, age, course, email) values (?, ?, ?, ?)',
                     (student.name, student.age, student.course, student.email))
        conn.commit()
        conn.close()

    # update student details
    def update_details(self, id, student):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''UPDATE student
               SET name = ?, age = ?, course = ?, email = ?
               WHERE id = ?''',
            (student.name, student.age, student.course, student.email, id))
        conn.commit()
        conn.close()

    # view student details
    def view_student(self):
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("select * from student")
        data = cur.fetchall()
        return data 

    # delete student from the table 
    def delete_student(self, id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM student WHERE id = ?', (id,))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    obj = Service()
    obj.create_table()
    print("student table created successfully")

    # add student 
    s = Student(1, "avani", 22, "DE", "avani@gmail.com")
    obj.add_student(s)
    print("student detail addess successfully")

    # view all student
    data = obj.view_student()
    print("data is: ")
    print(data)

    # delete student 
    obj.delete_student(1) 

    # view student after deletion
    data = obj.view_student()
    print("Data after deletion: ")
    print(data)