# 1. Combine both multiple and multilevel inheritance in a single program and demonstrate method
# calls.
class A:
    def method_A(self):
        print("This is Class A")
class B(A):   
    def method_B(self):
        print("This is Class B")
class C(A):   
    def method_C(self):
        print("This is Class C")
class D(B, C):   
    def method_D(self):
        print("This is Class D")
obj = D()
obj.method_A()
obj.method_B()
obj.method_C()
obj.method_D()

print()

# 2. Create a diamond problem scenario and resolve it using Python’s MRO.
class A:
    def show(self):
        print("This is Class A")
class B(A):
    def show(self):
        print("This is Class B")
class C(A):
    def show(self):
        print("This is Class C")
class D(B, C):
    pass
obj = D()
obj.show()

print()

# 3. Write a program to print the MRO of a complex inheritance structure.
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
class E(D):
    pass
print("MRO of class E:")
for cls in E.__mro__:
    print(cls)

print()

# 4. Create a system where one class inherits from two classes, and one of those classes further
# inherits from another (hybrid inheritance).
class A:
    def feature_A(self):
        print("Feature from A")
class B(A):
    def feature_B(self):
        print("Feature from B")
class C:
    def feature_C(self):
        print("Feature from C")
class D(B, C):
    def feature_D(self):
        print("Feature from D")
obj = D()
obj.feature_A()  
obj.feature_B()  
obj.feature_C()  
obj.feature_D()  
print("\nMRO of class D:")
for cls in D.__mro__:
    print(cls)

print()

# 5. Build a mini project: Employee management system using both inheritance types.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_person(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary
    def show_employee(self):
        print(f"ID: {self.emp_id}, Salary: {self.salary}")
class Manager(Employee):
    def manage_team(self):
        print(f"{self.name} is managing the team.")
class HR(Employee):
    def manage_payroll(self):
        print(f"{self.name} is managing payroll.")
class Admin(Manager, HR):
    def admin_task(self):
        print(f"{self.name} is doing admin tasks.")
admin1 = Admin("Avani", 25, 101, 50000)
admin1.show_person()
admin1.show_employee()
admin1.manage_team()
admin1.manage_payroll()
admin1.admin_task()
print("\nMRO of Admin class:")
for cls in Admin.__mro__:
    print(cls)