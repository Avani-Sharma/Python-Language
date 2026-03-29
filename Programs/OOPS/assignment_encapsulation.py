# 1. Create a class Person with a private variable __name. Create methods to set and get the name.
class Person:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name 
    def set_name(self, name):
        self.__name = name 
P1 = Person('avani')
print(P1.get_name())        # access through getter method
P1.set_name('hemant')       # change through setter method
print(P1.get_name()) 

print()

# Create a class BankAccount with private variable __balance. Add methods deposit(amount),
# withdraw(amount), and get_balance().
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount>0:
            self.__balance +=amount
            print(f"deposited: {amount}")
        else:
            print("invalid amount")
    def withdraw(self, amount):
        if amount>0 and amount <=self.__balance:
            self.__balance -= amount
            print(f"withdraw: {amount}")
        else:
            print("invalid amount")
    def get_balance(self):
        return self.__balance
account1 = BankAccount(1000)
account1.deposit(500)
account1.withdraw(300)
print(account1.get_balance())

print()

# Create a class Student with private variable __marks. Add methods to assign and display marks
# only if marks are greater than 0.
class Student:
    def __init__(self, marks):
        self.__marks = 0  
        if marks > 0:
            self.__marks = marks
        else:
            print("Invalid marks")
    def set_marks(self, marks):
        if marks > 0:
            self.__marks = marks
        else:
            print("Invalid marks")
    def get_marks(self):
        return self.__marks
S1 = Student(95)
print(S1.get_marks()) 
S1.set_marks(80)
print(S1.get_marks())  

print()

# Create a class Employee with private variable __salary. Add methods to set salary, increase
# salary by percentage, and get salary.
class Employee:
    def __init__(self, salary):
        self.__salary = salary 
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")
    def increase_salary(self, percent):
        if percent > 0:
            increment = self.__salary * percent / 100
            self.__salary += increment
        else:
            print("Invalid percentage")
E1 = Employee(40000)
print(E1.get_salary())   
E1.set_salary(50000)
print(E1.get_salary())   
E1.increase_salary(10)   
print(E1.get_salary())  

print()

# Create a class Temperature with private variable __celsius. Add methods to set temperature and
# convert it to Fahrenheit.
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    def convert_fahrenheit(self):
        Fahrenheit = (self.__celsius*9/5) + 32
        return Fahrenheit
    def get_celsius(self):
        return self.__celsius
    def set_celsius(self, celsius):
        if celsius > -273:  
            self.__celsius = celsius
        else:
            print("Invalid temperature")
T1 = Temperature(45)
print(T1.get_celsius())
print(T1.convert_fahrenheit())
T1.set_celsius(25)
print(T1.get_celsius())
print(T1.convert_fahrenheit())

print()

# Create a class Mobile with private variable __price. Add methods to set price (not negative) and get price.
class Mobile:
    def __init__(self, price):
        self.__price = price
    def get_price(self):
        return self.__price
    def set_price(self, price):
        if price >0:
            self.__price = price
        else:
            print("invalid price /not negative")
M1 = Mobile(6000)
print(M1.get_price())
M1.set_price(7000)
print(M1.get_price())

print()

# Create a class Car with private variable __speed. Add methods set_speed(speed <= 200) and get_speed().
class Car:
    def __init__(self, speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        if speed<=200:
            self.__speed = speed
        else:
            print("invalid speed")
C1 = Car(80)
print(C1.get_speed())
C1.set_speed(220)
print(C1.get_speed())    

print()

# Create a class LoginSystem with private variable __password. Add methods to set and validate password.
class LoginSystem:
    def __init__(self, password):
        self.__password = password
    def get_password(self):
        return self.__password
    def set_password(self, password):
        if len(str(password)) >= 4:   # basic validation
            self.__password = password
        else:
            print("Weak password")
    def validate_password(self, password):
        if self.__password == password:
            print("Login Successful")
        else:
            print("Wrong Password")
L1 = LoginSystem(4598)
print(L1.get_password())
L1.set_password(3456)
print(L1.get_password())
L1.validate_password(3456)
L1.validate_password(1111) 

print()

# Create a class Product with private variable __quantity. Add methods to add stock, reduce stock
# (not below 0), and check quantity.
class Product:
    def __init__(self, quantity):
        self.__quantity = quantity
    def add_stock(self, stock):
        if stock > 0:
            self.__quantity += stock
        else:
            print("Invalid stock")
    def reduce_stock(self, stock):
        if stock > 0 and self.__quantity - stock >= 0:
            self.__quantity -= stock
        else:
            print("Not enough stock or invalid value")
    def check_quantity(self):
        return self.__quantity
P1 = Product(50)
print(P1.check_quantity())  
P1.add_stock(20)
print(P1.check_quantity())   
P1.reduce_stock(30)
print(P1.check_quantity())  
P1.reduce_stock(100) 

print()

# Create a class VotingSystem with private variable __age. Add methods to set age and check if
# user can vote (>=18).
class VotingSystem:
    def __init__(self, age):
        self.__age = age
    def get_age(self):
        return self.__age 
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")
    def can_vote(self):
        if self.__age >= 18:
            print("User can vote")
        else:
            print("User can't vote")
V1 = VotingSystem(23)
print(V1.get_age())  
V1.can_vote()         
V1.set_age(17)
print(V1.get_age()) 
V1.can_vote()