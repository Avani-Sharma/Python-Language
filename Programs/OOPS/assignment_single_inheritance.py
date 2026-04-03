# Instructions (for all questions):
# 1 Create both parent and child class
# 2 Use __init__() in both classes
# 3 Use super() inside child constructor
# 4 Create at least one object
# 5 Create a display() method in child class
# 6 Print output in readable format

# ques1. Vehicle → Car
# Vehicle: brand, speed. Car: fuel_type. Use super(). Display all.
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type
    def display(self):
        print("Car brand: ", self.brand)
        print("Car speed: ", self.speed, "km/h")
        print("Car fuel_type: ", self.fuel_type)
C1 = Car("Nexon", 180, "Diesel")
C1.display()

print()

# ques2. Person → Teacher
# Person: name, age. Teacher: subject. Use super(). Display all.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def display(self):
        print("name: ", self.name)
        print("age: ", self.age)
        print("subject :", self.subject)
T1 = Teacher('avani', 21, 'python')
T1.display()

print()

# ques3. Employee → Manager
# Employee: emp_id, salary. Manager: department. Use super().
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary
class Manager(Employee):
    def __init__(self, emp_id, salary, department):
        super().__init__(emp_id, salary)
        self.department = department
    def display(self):
        print("emp_id: ", self.emp_id)
        print("salary: ", self.salary)
        print("department: ", self.department)
M1 = Manager(123, 70000, 'IT')
M1.display()

print()

# ques4. Product → Electronics
# Product: name, price. Electronics: warranty_years. Use super().
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Electronics(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years
    def display(self):
        print("name: ", self.name)
        print("price: ", self.price)
        print("warranty years: ", self.warranty_years)
E1 = Electronics('AC', 30000, 5)
E1.display()

print()

# ques5. Animal → Dog
# Animal: name, species. Dog: breed. Use super().
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    def display(self):
        print("name: ", self.name)
        print("species: ", self.species)
        print("breed: ", self.breed)
D1 = Dog('bruno', 'dog', 'Labrador')
D1.display()

print()

# ques6. Account → SavingsAccount
# Account: account_number, balance. SavingsAccount: interest_rate. Use super().
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
class SavingsAccount(Account):
    def __init__(self, account_number, balance, SavingsAccount):
        super().__init__(account_number, balance)
        self.SavingsAccount = SavingsAccount
    def display(self):
        print("account number: ", self.account_number)
        print("Balance: ", self.balance)
        print("Saving Account: ", self.SavingsAccount)
S1 = SavingsAccount(2134565, 40000, 456564)
S1.display()

print()

# ques7. User → Admin
# User: username, email. Admin: permissions. Use super().
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
class Admin(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions
    def display(self):
        print("Username:", self.username)
        print("Email:", self.email)
        print("Permissions:", self.permissions)
u1 = Admin('avani', 'abc12@gmail.com', 'yes')
u1.display()

print()

# ques8. Book → Ebook
# Book: title, author. Ebook: file_size. Use super().
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def display(self):
        print("title: ", self.title)
        print("author: ", self.author)
        print("file size: ", self.file_size)
E1 = Ebook("Python Basics", "Avani", "5MB")
E1.display()

print()

# ques9. Appliance → WashingMachine
# Appliance: brand, power. WashingMachine: capacity. Use super().
class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
class WashingMachine(Appliance):
    def __init__(self, brand, power, capacity):
        super().__init__(brand, power)
        self.capacity = capacity
    def display(self):
        print("brand: ", self.brand)
        print("power: ", self.power)
        print("capacity: ", self.capacity)
W1 = WashingMachine("LG", "500W", "7kg")
W1.display()

print()

# ques10. Shape → Circle
# Shape: color. Circle: radius. Use super().
class Shape:
    def __init__(self, color):
        self.color = color
class Circle(Shape):
    def __init__(self, color , radius):
        super().__init__(color)
        self.radius = radius
    def display(self):
        print("color: ", self.color)
        print("radius: ", self.radius)
C1 = Circle('black', 6)
C1.display()

print()

# ques11. Device → Laptop
# Device: name, price. Laptop: ram. Use super().
class Device:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Laptop(Device):
    def __init__(self, name, price, ram):
        super().__init__(name, price)
        self.ram = ram
    def display(self):
        print("name: ", self.name)
        print("price: ", self.price)
        print("ram: ", self.ram)
L1 = Laptop('Dell', 50000, 128)
L1.display()

print()

# ques12. Food → Fruit
# Food: name, calories. Fruit: vitamin_content. Use super().
class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
class Fruit(Food):
    def __init__(self, name, calories, vitamin_content):
        super().__init__(name, calories)
        self.vitamin_content = vitamin_content
    def display(self):
        print("name: ", self.name)
        print("calories: ", self.calories)
        print("vitamin content: ", self.vitamin_content)
F1 = Fruit("Apple", 95, "Vitamin C")
F1.display()

print()

# ques13. Company → Startup
# Company: name, location. Startup: funding_amount. Use super().
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location
class Startup(Company):
    def __init__(self, name, location, funding_amount):
        super().__init__(name, location)
        self.funding_amount = funding_amount
    def display(self):
        print("name: ", self.name)
        print("location: ", self.location)
        print("funding amount: ", self.funding_amount)
S1 = Startup('xyz', 'jaipur', '5 crore')
S1.display()

print()

# ques14. Movie → WebSeries
# Movie: title, duration. WebSeries: number_of_seasons. Use super().
class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
class WebSeries(Movie):
    def __init__(self, title, duration, number_of_seasons):
        super().__init__(title, duration)
        self.number_of_seasons = number_of_seasons
    def display(self):
        print("title: ", self.title)
        print("duration: ", self.duration)
        print("number of seasons : ", self.number_of_seasons)
W1 = WebSeries('abc', '30 min', 4)
W1.display()

print()

# ques15. Bank → Loan
# Bank: name, branch. Loan: loan_amount. Use super().
class Bank:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
class Loan(Bank):
    def __init__(self, name, branch, loan_amount):
        super().__init__(name, branch)
        self.loan_amount = loan_amount
    def display(self):
        print("name: ", self.name)
        print("branch: ", self.branch)
        print("loan amount: ", self.loan_amount)
L1 = Loan('study', 'SBI', 50000)
L1.display()

print()

# ques16. Course → OnlineCourse
# Course: course_name, duration. OnlineCourse: platform. Use super().
class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
class OnlineCourse(Course):
    def __init__(self, name, duration, platform):
        super().__init__(name, duration)
        self.platform = platform
    def display(self):
        print("name: ", self.name)
        print("duration: ", self.duration)
        print("platform: ", self.platform)
O1 = OnlineCourse('python', '3 months', 'internshala')
O1.display()

print()

# ques17. Game → MobileGame
# Game: title, genre. MobileGame: size. Use super().
class Game:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
class MobileGame(Game):
    def __init__(self, title, genre, size):
        super().__init__(title, genre)
        self.size = size
    def display(self):
        print("title: ", self.title)
        print("genre: ", self.genre)
        print("size: ", self.size)
M1 = MobileGame("BGMI", "Action", "2GB")
M1.display()

print()

# ques18. Hospital → Doctor
# Hospital: name, location. Doctor: specialization. Use super().
class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
class Doctor(Hospital):
    def __init__(self, name, location, specialization):
        super().__init__(name, location)
        self.specialization = specialization
    def display(self):
        print("name: ", self.name)
        print("location: ", self.location)
        print("specialization: ", self.specialization)
D1 = Doctor('Avani', 'Jaipur', 'Cardiologist')
D1.display()

print()

# ques19. Transport → Bus
# Transport: mode, fare. Bus: route_number. Use super().
class Transport:
    def __init__(self, mode, fare):
        self.mode = mode
        self.fare = fare
class Bus(Transport):
    def __init__(self, mode, fare, route_number):
        super().__init__(mode, fare)
        self.route_number = route_number
    def display(self):
        print("mode: ", self.mode)
        print("fare: ", self.fare)
        print("route number: ", self.route_number)
B1 = Bus("Bus", 50, "RJ14-101")
B1.display()

print()

# ques20. Clothing → Shirt
# Clothing: brand, size. Shirt: color. Use super().
class Clothing:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
class Shirt(Clothing):
    def __init__(self, brand, size, color):
        super().__init__(brand, size)
        self.color = color
    def display(self):
        print("brand: ", self.brand)
        print("size: ", self.size)
        print("color: ", self.color)
S1 = Shirt('zara', 'L', 'black')
S1.display()