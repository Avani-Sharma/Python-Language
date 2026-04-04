# 1. Create a base class Animal with a method sound(). Then create three child classes Dog, Cat, and
# Cow that override the sound() method to print their respective sounds. Write a main program where you
# create objects of each class and call the sound() method using a parent class reference to demonstrate
# runtime polymorphism.
class Animal:
    def make_sound(self):
        print("animal makes sound")
class Dog(Animal):
    def make_sound(self):
        print("barks")
class Cat(Animal):
    def make_sound(self):
        print("meow")
class Cow(Animal):
    def make_sound(self):
        print("cow makes sound")
obj = Dog()
obj1 = Cat()
obj2 = Cow()
obj.make_sound()
obj1.make_sound()
obj2.make_sound()

print()

# 2. Create a base class Vehicle with a method start(). Then create child classes Car, Bike, and Truck
# that override the start() method with their own implementation. Demonstrate how the correct method is
# called at runtime when using a common reference.
class Vehicle:
    def start_method(self):
        print("vehicle starts")
class Car(Vehicle):
    def start_method(self):
        print("Car starts")
class Bike(Vehicle):
    def start_method(self):
        print("Bike starts")
class Truck(Vehicle):
    def start_method(self):
        print("truck starts")
ob = Car()
ob1 = Bike()
ob2 = Truck()
ob.start_method()
ob1.start_method()
ob2.start_method()

print()

# 3. Create a base class Employee with a method salary(). Then create subclasses FullTimeEmployee
# and PartTimeEmployee. Override the salary() method in each subclass to calculate salary differently.
# Demonstrate runtime polymorphism using these classes.
class Employee:
    def emp_method(self):
        print("employee salary")
class FullTimeEmployee(Employee):
    def emp_method(self):
        print("full time employee salary")
class PartTimeEmployee(Employee):
    def emp_method(self):
        print("part time employee salary")
obje = FullTimeEmployee()
obje1 = PartTimeEmployee()
obje.emp_method()
obje1.emp_method()

print()

# 4. Create a base class SmartDevice with a method operate(). Then create subclasses SmartLight,
# SmartTV, and SmartSpeaker. Override operate() to perform device-specific actions. Demonstrate
# runtime polymorphism using a list of objects.
class SmartDevice:
    def operate(self):
        print("Operating a generic smart device")
class SmartLight(SmartDevice):
    def operate(self):
        print("Smart Light is turned ON")
class SmartTV(SmartDevice):
    def operate(self):
        print("Smart TV is playing a movie")
class SmartSpeaker(SmartDevice):
    def operate(self):
        print("Smart Speaker is playing music")
devices = [SmartLight(), SmartTV(), SmartSpeaker()]
for device in devices:
    device.operate()  

print()

