# inheritance = it is the property of oops or one of the four pillars which makes the 
# parent class  accessible to the child class
#1.single inheritance
#2. multiple inheritance
#3. multilevel inheritance
#4.hybrid inheritance

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