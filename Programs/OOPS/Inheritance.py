# inheritance = it is the property of oops or one of the four pillars which makes the 
# parent class  accessible to the child class
#1. single inheritance
#2. multiple inheritance
#3. multilevel inheritance
#4. hybrid inheritance

#ex. property of the father is inheritate to the child .
# in inheritance all the attributes and the methods are inherited to the class 
class Father:  
    highwayproperty = "property"
    def fatherproperty(self):
        print("this is the access to the property of the father")
class Child(Father): # here we have inherited form the father to the child
    pass
child = Child()
# here we have access in the fathers property
child.fatherproperty()

class Employee:
    company  = 'tcs'  # class attribute
    def __init__(self,name,salary,gender):
        self.name  = name
        self.salary  = salary
        self.gender = gender
class Developer(Employee):  # refers to parent memory this is child
    pass
obj = Developer('shyam',20000,"male")  # object in  the child name 
print(obj.gender)    # for individual use print
                
                
class Employee:   # parent class name
    company = 'tcs'   # class attribute
    def __init__(self,name,salary,gender):  # parent constructor
        self.name = name
        self.salary = salary
        self.gender = gender
class Developer(Employee):  # child class name with parent name() to get access
    def __init__(self,name,salary,gender,department):
        #using the super() keryword we initialised the parent instance attribute
        super().__init__(name,salary,gender) # according to parent parameters use super instead of self
        self.department = department  # extra you want acc to child not parent
obj = Developer('shyam',20000,'male','software engineer')  # child memory object 
print(obj.name)
print(obj.department)            
print(obj.gender) 
print(obj.company)   # because it is class attribute it is common for all

print()

# multilevel inheritance: Multilevel inheritance is a type of inheritance in which a class is derived 
# from a parent class, and that parent class is itself derived from another class. 
# or basically there more than one level of inheritance is given.
# It forms a chain of inheritance.
# Example chain: Grandparent → Parent → Child.
# example
class GrandFather:
    grandfather_prop = "grandfather's property"
class Father(GrandFather):
    father_prop = "father's property"
class Child(Father):
    child_prop = "child's property"
obj = Child()
print(obj.grandfather_prop)

# real life example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, dep):
        super().__init__(name, age)
        self.dep = dep
class Manager(Employee):
    def __init__(self, name, age, dep, team_size):
        super().__init__(name, age, dep)
        self.team_size = team_size
    def details(self):
        print(f"name is: ", self.name)
        print(f"age is: ", self.age)
        print(f"dep is: ", self.dep)
        print(f"team size is: ", self.team_size)
manager = Manager("avani", 21, 'IT', 50)
manager.details()

print()

# multiple inheritance: in this inheritance basically there is more than one parent of the derived class 
# or the child class 
# example: class A, class B, class(A, B)
# __mro__ : means method resolution order : define or decides how the method od different class would run.
# A - Display method
# B - Display method
# C(A, B)
# C - obj-> obj.display -> here class A display method is called.
# class -> C , class A, class B
class CngCar:
    cng_prop = 'this car will run with cng'
    def display(self):
        print("this is the cng car property")
class PetrolCar:
    petrol_prop = 'this car will run with petrol'
    def display(self):
        print("this is the petrol car property")
class HybridCar(PetrolCar, CngCar):
    pass
car = HybridCar()
car.display()

