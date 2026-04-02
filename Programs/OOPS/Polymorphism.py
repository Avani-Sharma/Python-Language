# Polymorphism: poly means many and morphism means forms 
# it is one of the most important pillar of OOPS. in which a function or method have many forms
# there are two types of polymorphism: 
# 1. compile time polymorphism (method overloading): feature where a class has multiple methods with 
# the same name but different parameters(numbers, type or order). 
# why python doesn't support method overloading: due to its dynamic nature and the way it manages name.
# like name overwrite.

# 2. run time polymorphism (method overriding): where a subclass provide its own specific implementation
# of a method that is already defined in its parent class. 
class Animal:
    def make_sound(self):
        print("animal makes sound")
class Dog(Animal):
    def make_sound(self):
        print("barks")
obj = Dog()
obj.make_sound()

# Operator overloading: using the same operator for different data type. Python allows operators 
# like +, *, etc., to be overloaded using special methods (__add__, __mul__, etc.). It enables operators
#  to work with user-defined objects.
class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Number(self.value + other.value)
    def __str__(self):
        return str(self.value)
num1 = Number(10)
num2 = Number(20)
result = num1 + num2 
print(result)  
