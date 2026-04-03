# abstraction: In Python, abstraction is a fundamental Object-Oriented Programming (OOP) principle 
# used to hide complex implementation details and expose only the essential features of an object.

# abstract class:  is a blueprint for other classes that cannot be instantiated on its own. It is used to define
# a common interface that all subclasses must follow, ensuring they implement specific methods.
# what is abstract base class: in python abc stands for abstract base class. It is a module in python standard 
# library used to define blueprint for other.
# Enforced Interfaces: If a class inherits from an ABC and does not implement all of its "abstract methods," 
# Python will raise a TypeError when you try to create an instance of that class.

# example
# here we have imported the ABC(helper class) and abstract method the module abc.
from abc import ABC, abstractmethod
# here we have created a vehicle class (interface or abstract base class)
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class EvCar(Vehicle):
    def start(self):
        print("the car starts!")
    def stop(self):
        print("the car stop!")
class PetrolCar(Vehicle):
    def start(self):
        print("petrol car starts!")
    def stop(self):
        print("car Stop")
obj = EvCar()
obj1 = PetrolCar()
obj.start()
obj1.start()