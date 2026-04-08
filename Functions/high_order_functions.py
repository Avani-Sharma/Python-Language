# high order function: are the functions which are used to call another function as an parameter.
# in the high order function we basically pass other function as an argument as  an argument 
# of another function 

def hello(fun):
    print("hello from hello function")
    fun()
def fun():
    print("hello from function")
hello(fun)

print()

# another example:
def operate(func):
    print("Inside operate function")
    func()
def greet():
    print("Good Morning")
operate(greet)

print()

# into the high order function we can define the another function also.
def outer():
    print("outer function is running")
    def inner():
        print("inner function is running")
    inner()
outer()

# create a high order function that filter outs the even numbers from the list 
def high_fun(fun, list):
    result = []
    for num in li:
        if fun(num):
            result.append(num)
    return result
def is_even(n):
    if n%2==0:
        return True
    return False
print(is_even(10))
li = [1,2,3,4,5]
ans = high_fun(is_even, li)
print(ans)

# filter out negative numbers from the list 
def high_fun(fun, list):
    result = []
    for num in li:
        if fun(num):
            result.append(num)
    return result
def is_negative(n):
    if n<0:
        return True
    return False
print(is_negative(-4))
li = [1,-2,-3,4,5]
ans = high_fun(is_negative, li)
print(ans)