class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def display(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')
        print(f'marks: {self.marks}')

def calculate_percentage(obtained_marks, total):
    return (obtained_marks/total) * 100