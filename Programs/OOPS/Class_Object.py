# class: is a blueprint of the object that helps in making object
# object: is a real world entity which has some attributes and properties
# ex: the house is the object which is made by the help of  class

# class attributes is same for every object
#constructor is a method which is called automatically when we initialised the object
# or create the object .it allocates the memory to objects or the attributes
#class attribue = this is same for all the object
# self it refers to the current object reference

# example
class Blueprint:
    location = "jaipur"   # same for all
    def __init__(self,color,no_rooms):
        self.color  = color
        self.no_rooms = no_rooms
house1 = Blueprint("blue",4)
print(f"the color of house of :{house1.color} and no of room is {house1.no_rooms}")
print(house1.color,house1.no_rooms) 
house2 = Blueprint("red",5)
print(house2.color,house2.no_rooms)   


# example
class Employee:
    company = "tcs"
    def __init__(self,emp_id,name,gender,salary):
        self.emp_id = emp_id
        self.name = name
        self.gender = gender
        self.salary = salary
    def display(self):
        print(f"emp id = {self.emp_id}")
        print(f"empname = {self.name}")
        print(f"emp gender= {self.gender}")
        print(f"salary = {self.salary}")
emp1 = Employee(1223,"vishal","male",20000)
emp1.display()  

# 1. create a class of student like  which have some properties like student name,location,id,
# branch,collegename.
class Student():
    def __init__(self,name,location,id,branch,collegename):
        self.name  = name
        self.location = location
        self.id = id
        self.branch = branch
        self.collegename = collegename
student1 = Student("madhav","jaipur",123,"regex","jecrc") 
print(student1.name) 
print(student1.location) 
print(student1.id) 
print(student1.branch) 
print(student1.collegename) 


# 2. create two student object and print their details using the method with comment
class Student():
    def __init__(self,name,location,id,branch,collegename):
        self.name  = name
        self.location = location
        self.id = id
        self.branch = branch
        self.collegename = collegename
    def display(self):
        print(f"studentname = {self.name}")
        print(f"studentlocation = {self.location}")
        print(f"studentid = {self.id}")
        print(f"studentbranch = {self.branch}")
        print(f"studentcollegename= {self.collegename}")
student1 = Student("dhruv","jaipur",123,"regex","jecrc")
student2 = Student("keshav","delhi",1122,"regex2","matsya")
student1.display()
student2.display ()    