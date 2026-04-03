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
obj = Dog()
obj.make_sound()