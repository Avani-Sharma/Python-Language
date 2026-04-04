# encapsulation: a fundamental concept of Object-Oriented Programming (OOP) that involves bundling data 
# (attributes) and methods that operate on that data into a single unit, typically a class.

# or 

# encapsulation is the way to wrap the data (variable) and methods into the single unit (single class) so, it's 
# access could be restricted.

# private attributes: are the attributes which is not accessible outside of the class.
# private attributes are initialized with double underscores '__'.
# ex: bank balance, password, etc.

# Marks Management System
class Student:
    def __init__(self, marks, name, id):
        # private attribute
        self.__marks = marks
        self.name = name
        self.id = id
obj = Student(40, 'avani', 'abcd')
print(obj.name)
print(obj.id)


# protected attribute: initialized with one underscore '_'.

# ATM management system 
class ATM:
    def __init__(self, pin, name, balance):
        # private attributes
        self.__pin = pin 
        # public attributes
        self.name = name 
        # protected attributes
        self._balance = balance 
    # getter method is used to get the values of the private and protected attribute of the class.
    # this display method is accessing the protected attribute 
    def display_balance(self):
        balance = self._balance
        print(f'the balance is: {balance}')
    # to change the pin of atm card
    # this change pin is setter method which is used to set or change or update the value of 
    # private attribute.
    def change_pin(self, new_pin):
        self.__pin = new_pin
        print("pin change successfully")
# creating the pin of the card
obj = ATM(1234, 'avani', 50000)
obj.display_balance()
obj.change_pin(9876)

# account management system 
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def display_balance(self):
        balance = self.__balance
        print(balance)
    def deposit(self, amount):
        self.__balance += amount
        print("money deposited successfully")
# opening account
acc1 = BankAccount('avani', 5000)
acc1.display_balance()
acc1.deposit(5000)
acc1.display_balance()


# ques:-  create a class librarybook that demonstrate the encapsulation. 
# Create a private variable no_available_book 
# make a method to issue a book (decrease the no. of books if books are available otherwise print
# the 'not available book')
# make a method to check how many books are available.
class LibraryBook:
    def __init__(self, total_books):
        # private variable
        self.__no_available_book = total_books
    # method to issue book
    def issue_book(self):
        if self.__no_available_book > 0:
            self.__no_available_book -= 1
            print("Book issued successfully")
        else:
            print("Not available book")
    # method to check available books
    def check_books(self):
        return self.__no_available_book
# object create
obj = LibraryBook(3)
obj.issue_book()
obj.issue_book()
obj.issue_book()
obj.issue_book()   
print("Available books:", obj.check_books())