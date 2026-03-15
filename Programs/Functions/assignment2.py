# map questions:
# 1 Write a program that takes a list of integers and uses map to return a new list containing the
# square of each number.
li = [1,2,3,4]
def sq(x):
    return x**2
print(list(map(sq, li)))

# 2 Given a list of temperatures in Celsius, use map to convert them into Fahrenheit. 
# (Formula: F = (C × 9/5) + 32)
li = [0, 20, 34, 45]
def convert(C):
    return (C*9/5)+32
print(list(map(convert, li)))

# 3 Take a list of strings and use map to convert each string into its uppercase form.
li = ['avani', 'chinki']
def st(s):
    return s.upper()
print(list(map(st, li)))

# 4 Given a list of numbers, use map with a lambda function to add 10 to each element and print
# the updated list.
li = [10, 20, 30, 40]
result = list(map(lambda a: a+10, li))
print(result)

# 5 Write a program that takes two lists of equal length and uses map to return a list containing the
# sum of corresponding elements.
l1 = [1,2,3,4]
l2 = [5,6,7,8]
def fun(y, z):
    return y+z
result = list(map(fun, l1, l2) )
print(result)



# filter questions: 
# 1 Given a list of integers, use filter to create a new list containing only even numbers.
li = [1,2,3,4,5,6]
def even(r):
    return r%2==0
result = list(filter(even, li))
print(result)

# 2 Write a program that takes a list of numbers and filters out all numbers greater than 50.
li = [20, 30, 40 , 60, 80, 90]
def greater(g):
    return g>50
result = list(filter(greater, li))
print(result)

# 3 Given a list of strings, use filter to return only those strings whose length is greater than 5.
li = ['Avani', 'chinki']
def leng(l):
    return len(l)>5
result = list(filter(leng, li))
print(result)

# 4 Write a program to filter out all negative numbers from a given list using filter and lambda.
li = [1,2,-1,-2,-3, -5]
result = list(filter(lambda ng: ng<0, li ))
print(result)

# 5 Given a list of integers, use filter to extract only numbers that are divisible by both 2 and 3.
li = [4, 6,12, 18, 9, 15]
def div(d):
    return d%2==0 and d%3==0
result = list(filter(div, li))
print(result)



# higher order function questions:
# 1 Write a function calculate that takes another function and a number as arguments and applies
# that function to the number.
# 2 Create a function operation that accepts two numbers and a function (like add, multiply) and
# returns the result after applying the function.
# 3 Write a function power_generator that returns another function which calculates the cube of a
# number.
# 4 Create a function apply_twice that takes a function and a number, and applies the function two
# times on the number.
# 5 Write a function choose_function that takes a string argument ('double' or 'triple') and returns a
# corresponding function to multiply a number.



# decorator questions:
# 1 Write a decorator that prints 'Function started' before execution and 'Function ended' after
# execution of any function.
def deco(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper
@deco
def my_fun():
    print("fun")
my_fun()

# 2 Create a decorator that measures and prints the execution time of a function.

# 3 Write a decorator that checks whether the input number to a function is positive; if not, it should
# print an error message.
def pos(fun):
    def wrapper(m):
        if m>0:
            return fun(m)
        else:
            print("error ")
    return wrapper
@pos
def num(m):
    print(m)
m = int(input())
num(m)

# 4 Create a decorator that logs the arguments passed to a function before calling it.
def log_args(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper
@log_args
def add(a, b):
    print("Sum:", a + b)
add(5, 3)
 
# 5 Write a decorator that allows a function to be executed only once; on subsequent calls it should
# print 'Function already executed'.
def run_once(func):
    executed = False
    def wrapper():
        nonlocal executed
        if not executed:
            func()
            executed = True
        else:
            print("Function already executed")
    return wrapper
@run_once
def greet():
    print("Hello")
greet()
greet()
greet()
