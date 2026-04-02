# 1. Create class Grandparent, Parent, and Child. Add methods in each and show how child accesses all.
class Grandparent:
    def __init__(self):
        print("Grandparent constructor")
    def grandparent_method(self):
        print("This is Grandparent method")
class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent constructor")
    def parent_method(self):
        print("This is Parent method")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")
    def child_method(self):
        print("This is Child method")
obj = Child()
obj.grandparent_method()
obj.parent_method()
obj.child_method()

print()

# 2. Write a program where Animal → Mammal → Dog and each class has its own method. Call all
# methods using the Dog class.
class Animal:
    def __init__(self):
        print("animal constructor")
    def animal_method(self):
        print("animal method")
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal constructor ")
    def mammal_method(self):
        print("mammal method")
class Dog(Mammal):
    def __init__(self):
        super().__init__()
        print("Dog constuctor")
    def dog_method(self):
        print("dog method")
obj2 = Dog()
obj2.animal_method()
obj2.mammal_method()
obj2.dog_method()

print()

# 3. Create a class Vehicle, then Car inherits from it, and SportsCar inherits from Car. Add methods
# at each level.
class Vehicle:
    def __init__(self):
        print("vehicle constructor")
    def vehicle_method(self):
        print("this is vehicle method")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("car constructor")
    def car_method(self):
        print("this is car method")
class SportsCar(Car):
    def __init__(self):
        super().__init__()
        print("sportscar constructor")
    def sportscar_method(self):
        print("this is sportscar method")
obj3 = SportsCar()
obj3.vehicle_method()
obj3.car_method()
obj3.sportscar_method()

print()

# 4. Demonstrate constructor chaining in multilevel inheritance using super().
class A:
    def __init__(self):
        print("constructor A")
class B(A):
    def __init__(self):
        super().__init__()
        print("constructor B")
class C(B):
    def __init__(self):
        super().__init__()
        print("constructor C")
obj4 = C()

print()

# 5. Create a class Shape → Rectangle → Square and calculate area at each level.
class Shape:
    def __init__(self):
        print("Shape constructor")
    def area(self):
        print("Area not defined")
class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth
        print("rectangle constructor")
    def area(self):
        rec_area = self.length * self.breadth
        print("reactangle area: ", rec_area)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        print("square constructor")
    def area(self):
        sq_area = self.length * self.length
        print("Square area: ", sq_area)
obj5 = Square(5)
obj5.area()

print()

# 6. Write a program showing method overriding in multilevel inheritance.
class A:
    def show(self):
        print("Method from Class A")
class B(A):
    def show(self):
        print("Method from Class B")
class C(B):
    def show(self):
        print("Method from Class C")
obj = C()
obj.show()

print()

# 7. Create a class Student → GraduateStudent → PhDStudent and add attributes progressively.
class Student:
    def __init__(self, name):
        self.name = name
        print("Student constructor")
    def show_student(self):
        print("Name:", self.name)
class GraduateStudent(Student):
    def __init__(self, name, degree):
        super().__init__(name)
        self.degree = degree
        print("Graduate Student constructor")
    def show_graduate(self):
        print("Degree:", self.degree)
class PhDStudent(GraduateStudent):
    def __init__(self, name, degree, research_topic):
        super().__init__(name, degree)
        self.research_topic = research_topic
        print("PhD Student constructor")
    def show_phd(self):
        print("Research Topic:", self.research_topic)
obj7 = PhDStudent("Avani", "MSc", "Data Science")
obj7.show_student()
obj7.show_graduate()
obj7.show_phd()

print()

# 8. Implement a banking system: Account → SavingsAccount → FixedDepositAccount.
class Account:
    def __init__(self):
        print("account constuctor")
    
class SavingsAccount(Account):
    def __init__(self):
        print("saving account constructor")
class FixedDepositAccount(SavingsAccount):
    def __init__(self):
        print("fixed deposit account constuctor ")