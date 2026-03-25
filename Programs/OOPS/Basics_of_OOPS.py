# object oriented programming(oops) is a programming based on "objects" that contain data 
# and code ,used in real world entities.it aims to improve code reusability ,structure ,
# and maintainability through 
# four main principles-->encapsulation,abstraction,inheritance,polymorphism

# class is defined using the class keyword
class Car:  
#     # this is the class property with color variable we can put  multiple property
    color = "blue"   
#  here we write the object real entity which have some properties.
# to create the object of the class we basically use the class name()
object = Car()
# to access the propety use property name  with use of (.)
print(object.color)     

# example
class Car:
    # class attribute
    manufacture = "Suzuki"
    # constructor
    #when the object is instantiated then this constructor method is called to initialise the 
    # location memory reference of the particular object or instance attribute
    def __init__(self,color):
        self.colorname  = color
car1 = Car("white")
car2 = Car("blue")
print(car1.colorname)
print(car2.colorname)        


# example
class Student:
    college = "IIT"
    # make a constructor for every student
    def __init__(self,name,branch,location):
        self.student_name = name
        self.student_branch = branch
        self.student_location = location
student1 = Student('dhruv','bcom','jaipur')
print(student1.student_branch,student1.student_location)

# example
class Student:
    name = "dhruv"
    grade = 'b'
    location = "jaipur"      # fixed data for all types of objects
student1 = Student()
student2  = Student()
print(student1.name,student1.grade)
print(student2.name,student2.grade) 

# example
class Student:
    def __init__ (self,name,location,grade):
        self.name = name 
        self.location = location
        self.grade = grade
student1 = Student("dhruv","jaipur",'b')
student2 = Student("madhav","siliguri",'c')
print(student1.name,student1.grade,student1.location)  # order doesnot matter
print(student2.name,student2.location,student2.grade)