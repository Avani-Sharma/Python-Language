from Models.student import Student
from Services.student_service import Service

# Creating the object of the Service Class
ser = Service()
ser.create_table()

while True:
    print('1.Press 1 to add Student\n2.Press 2 to View all the students.\n3.Press 3 to update the student details.\n4.Press 4 to exit.')
    option = int(input('Enter the Option: '))
    if option == 1:
        id = input('Enter the Student ID: ')
        name = input('Enter the name of the student: ')
        age = int(input('Enter the age of the student: '))
        course = input('Enter the course detail of the student: ')
        email = input('Enter the email of the student: ')

        obj = Student(id, name, age, course, email)
        ser.add_student(obj)
        print('The student Added Successfully!')
    elif option == 2:
        data = ser.view_student()
        print(data)
    elif option == 3:
        id = int(input('Enter the id of the student: '))
        ser.delete(id)
        print('The student data deleted from the database!')
    else:
        print('Please Enter the valid input')
        break