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

# 5. Create a base class Transport with a method fare(distance). Then create subclasses Bus, Train,
# and Taxi. Override fare() with different fare calculation logic. Show polymorphism using different
# objects.
class Transport:
    def fare(self, distance):
        print("Base fare method")
class Bus(Transport):
    def fare(self, distance):
        return distance * 5  
class Train(Transport):
    def fare(self, distance):
        return distance * 3 
class Taxi(Transport):
    def fare(self, distance):
        return distance * 10 
ports = [Bus(), Train(), Taxi()]
distance = 10
for port in ports:
    print(port.__class__.__name__, "Fare:", port.fare(distance))

print()

# 6. Create a base class FileHandler with a method open(). Then create subclasses TextFile, ImageFile,
# and PDFFile. Override open() to simulate opening different file types. Demonstrate runtime
# polymorphism.
class FileHandler:
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