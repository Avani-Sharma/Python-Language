# Student Management System
from Student.Student_Ops import Student as s
from Student.Student_Ops import calculate_percentage

obj = s('avani', 23, 80)
obj.display()
per = calculate_percentage(80, 100)
print(f'{per}%')