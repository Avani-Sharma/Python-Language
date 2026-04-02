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
        print("Speaker speaks a lecture")
class Author(Writer, Speaker):
    def work(self):
        print("author do both work")
a = Author()
a.write()
a.speak()
a.work()

print()

# 5. Create two parent classes Calculator1 (addition) and Calculator2 (multiplication). Create a child
# class that uses both operations.

# 6. Demonstrate method overriding in multiple inheritance where both parent classes have a method
# with the same name.
# 7. Create a class A and B with constructors. Create class C inheriting from both and show how
# constructors are called.
# 8. Write a program to demonstrate the Method Resolution Order (MRO) in multiple inheritance.
# 9. Create two classes Person and Employee with attributes. Inherit both into Manager and display
# combined details.
# 10. Implement a class SmartDevice that inherits from both Phone and Camera and performs both
# calling and clicking photos.