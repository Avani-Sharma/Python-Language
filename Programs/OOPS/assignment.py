#1. Create a class called Student that has a class attribute school_name and
# instance attributes name and age which are initialized using a constructor. Create
# three objects and print both the class attribute and instance attributes for each
# object. 

class Student:
    schoolname = "abc"  
    def __init__(self,name,age):
        self.name = name
        self.age = age
student1 = Student("Madhav",23)
student2 = Student("shree",22)
student3 = Student("sheela",16)
print(student1.name,student1.age,student1.schoolname)
print(student2.name,student2.age,student2.schoolname)
print(student3.name,student3.age,student3.schoolname)

# 2. Create a class called Car that has a class attribute wheels set to 4. Use a
# constructor to initialize instance attributes brand and price. Create two objects and
# show how both objects share the same class attribute but have different instance
# attributes.

class Car:
    carwheels = 4
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
car1 = Car("suzuki","5 lakh")
car2 = Car ("jaquar","1crore")
print(car1.brand,car1.price,car1.carwheels)
print(car2.brand,car2.price,car2.carwheels)

# 3. Create a class called Employee that has a class attribute company_name.
# Initialize instance attributes emp_name and salary using a constructor. Create
# multiple employee objects and print their details along with the common company
# name.

class Employee:
    companyname = "xyz company"
    def __init__(self,name,salary):
        self.name = name
        self.salary  = salary
emp1= Employee("ayush",50000)
emp2 = Employee("keshav",80000)
print(emp1.name,emp1.salary,emp1.companyname)
print(emp2.name,emp2.salary,emp2.companyname)        
    
           
 
# 4. Create a class called Mobile that has a class attribute category set to
# Electronics. Use a constructor to initialize mobile_name and RAM. Create three
# objects and print all values to clearly understand class vs instance attributes. 

class Mobile:
    category = "android"
    def __init__(self,mobilename,ram):
        self.mobilename = mobilename
        self.ram = ram
m1 = Mobile("nothing","4gb")
m2 = Mobile("samsung","8gb")
m3 = Mobile("lenevo","4gb")
print(m1.mobilename,m1.ram,m1.category)
print(m2.mobilename,m2.ram,m2.category)
print(m3.mobilename,m3.ram,m3.category)

# 5. Create a class called Book that has a class attribute library_name. Initialize
# instance attributes title and author using a constructor. Create at least two objects
# and print their complete information.

class Book:
    libraryname = "swadhaye"
    def __init__(self,title,author):
        self.title = title
        self.author= author
x = Book("harrypotter","harry")
y = Book("fivepointsomeone","chetanbhagat")
print(x.title,x.author,x.libraryname)
print(y.title,y.author,y.libraryname)

# 6. Create a class called Laptop that has a class attribute warranty_years. Use a
# constructor to initialize brand and price. Create multiple laptop objects and display
# how the class attribute remains same for all objects. 

class Laptop:
    warranty = "5yr"
    def __init__(self,brand,price):
        self.brand= brand
        self.price = price
x=Laptop("lenevo",40000)
y = Laptop("asus",34000)
z  = Laptop ("apple",78000)
print(x.brand,x.price,x.warranty)
print(y.brand,y.price,y.warranty)
print(z.brand,z.price,z.warranty)  

#    7. Create a class called Person that has a class attribute country. Initialize instance
# attributes name and age using a constructor. Create three person objects and print
# their data. 

class Person:
    country = "india"
    def __init__(self,name,age):
        self.name = name
        self.age = age
person1 = Person("madhav",22)
person2 = Person("kunal",44)
person3 = Person("hamza",33)
print(person1.name,person2.age,person1.country)
print(person2.name,person2.age,person2.country)
print(person3.name,person3.age,person3.country)   

# 8. Create a class called Bike that has a class attribute type set to Two Wheeler.
# Use a constructor to initialize bike_name and mileage. Create objects and print all
# details.   

class Bike:
    type = "2 wheeler"
    def __init__(self,name,mileage):
        self.name = name
        self.mileage = mileage
person1 =Bike("honda",65)
person2 = Bike("tvs",66)
person3 = Bike("avengers",12)
print(person1.name,person1.mileage,person1.type) 
print(person2.name,person2.mileage,person2.type)
print(person3.name,person3.mileage,person3.type)         
            
# 9. Create a class called Movie that has a class attribute industry set to Bollywood.
# Initialize instance attributes movie_name and rating using a constructor. Create
# multiple movie objects and print the details.

class Movie:
    industry = "bollywood"
    def __init__(self,name,ratings):
        self.name= name
        self.ratings = ratings
movie1 = Movie("dhurandhar",5)
movie2 = Movie("dhooom1",4)
print(movie1.name,movie1.ratings,movie1.industry)
print(movie2.name,movie2.ratings,movie2.industry)                
                 
                 
# 10. Create a class called BankAccount that has a class attribute bank_name. Use
# a constructor to initialize account_holder and balance. Create two account objects
# and print their information showing both class and instance attributes.  

class BankAccount:
    bankname = "hdfc"
    def __init__(self,accountholder,balance):
        self.accountholder= accountholder
        self.balance = balance
person1 = BankAccount("dhruv","5crore")
person2 = BankAccount ("keshav","5crore")
print(person1.accountholder,person1.balance,person1.bankname)
print(person2.accountholder,person2.balance,person2.bankname)