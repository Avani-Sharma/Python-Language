# decorator: it is a high order function which make changes or modify the existing function without 
# changing the original code.
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
@my_decorator
def greet():
    print("Hello Avani")
greet()


# write a program to check input is positive or not and add the functionality into the power function
def positive(func):
    def wrapper(n):
        if n < 0:
            print("Number is not positive")
        else:
            return func(n)
    return wrapper
@positive
def power(n):
    return n ** 2
num = int(input("Enter a number: "))
result = power(num)
if result is not None:
    print("Power:", result)