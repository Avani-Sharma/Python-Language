# 1. Create two classes Father and Mother with methods skills_father() and skills_mother(). Create a
# child class Child that inherits from both and prints both skills.
# Parent Class 1
class Father:
    def skills_father(self):
        print("Father: Driving, Business")
class Mother:
    def skills_mother(self):
        print("Mother: Cooking, Painting")
class Child(Father, Mother):
    def skills_child(self):
        print("Child: Learning from both parents")
c = Child()
c.skills_father()
c.skills_mother()
c.skills_child()

print()

# 2. Write a program where class Teacher has a method teach() and class Researcher has a method
# research(). Create a class Professor that inherits from both and uses both methods.
class Teacher:
    def teach(self):
        print("Teacher is teaching")

class Researcher:
    def research(self):
        print("Researcher is doing research")

class Professor(Teacher, Researcher):
    def work(self):
        print("Professor is doing both teaching and research")
p = Professor()
p.teach()
p.research()
p.work()

print()

# 3. Create two classes Engine and ElectricSystem with respective methods. Create a class
# HybridCar that inherits from both and demonstrates both functionalities.
class Engine:
    def engine_method(self):
        print("Engine method")
class ElectricSystem:
    def electric_method(self):
        print("electric system method")
class HybridCar(Engine, ElectricSystem):
    def hybrid_method(self):
        print("hybrid car method")
h = HybridCar()
h.engine_method()
h.electric_method()
h.hybrid_method()

print()

# 4. Implement two classes Writer and Speaker with methods write() and speak(). Create a class
# Author that inherits from both and calls both methods.
class Writer:
    def write(self):
        print("Writes writes a story")
class Speaker:
    def speak(self):
        print("Speaker gives a lecture")
class Author(Writer, Speaker):
    def work(self):
        print("author does both")
a = Author()
a.write()
a.speak()
a.work()

print()

# 5. Create two parent classes Calculator1 (addition) and Calculator2 (multiplication). Create a child
# class that uses both operations.
class Calculator1:
    def addition(self, a, b):
        print("Addition:", a + b)
class Calculator2:
    def multiplication(self, a, b):
        print("Multiplication:", a * b)
class Child(Calculator1, Calculator2):
    def work(self):
        print("Child can perform both operations")
b = Child()
b.addition(5, 3)
b.multiplication(5, 3)
b.work()

print()

# 6. Demonstrate method overriding in multiple inheritance where both parent classes have a method
# with the same name.
class Parent1:
    def show(self):
        print("This is Parent1 show method")
class Parent2:
    def show(self):
        print("This is Parent2 show method")
class Child(Parent1, Parent2):
    def show(self):
        print("This is Child show method")
c = Child()
c.show()

print()

# 7. Create a class A and B with constructors. Create class C inheriting from both and show how
# constructors are called.
class A:
    def a_method(self):
        print("Its A constructor")
class B:
    def b_method(self):
        print("its B constructor ")
class C(A, B):
    def c_method(self):
        print("its C constructor ")
z = C()
z.a_method()
z.b_method()
z.c_method()

print()

# 8. Write a program to demonstrate the Method Resolution Order (MRO) in multiple inheritance.
class A:
    def a_method(self):
        print("Its A constructor")
class B:
    def b_method(self):
        print("its B constructor ")
class C(A, B):
    def c_method(self):
        print("its C constructor ")
z = C()
z.a_method()
z.b_method()
z.c_method()
print(C.__mro__)

print()

# 9. Create two classes Person and Employee with attributes. Inherit both into Manager and display
# combined details.
class Person:
    def per_method(self):
        print("learning python")
class Employee:
    def emp_method(self):
        print("employee doing his task")
class Manager(Person, Employee):
    def man_method(self):
        print("manager checks both work")
m = Manager()
m.per_method()
m.emp_method()
m.man_method()

print()

# 10. Implement a class SmartDevice that inherits from both Phone and Camera and performs both
# calling and clicking photos.
class Phone:
    def phn_method(self):
        print("phone calling")
class Camera:
    def cam_method(self):
        print("clicking photos")
class SmartDevice(Phone, Camera):
    def smrt_method(self):
        print("doing both")
s = SmartDevice()
s.phn_method()
s.cam_method()
s.smrt_method()