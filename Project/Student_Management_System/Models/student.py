class Student:
    def __init__(self, id, name, age, course, email):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.email = email
    
if __name__ == '__main__':
    obj = Student(1, 'avani', 22, 'DE', 'avani12@gmail.com')
    print(obj)