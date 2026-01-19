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