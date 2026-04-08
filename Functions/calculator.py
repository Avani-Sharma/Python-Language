# make a calculator using functions
# +, -, *,/, %
# high order functions: 
def add(a,b):
    return a+b 
def sub(a,b):
    return a-b 
def mul(a,b):
    return a*b 
def div(a,b):
    return a/b 
def mod(a,b):
    return a%b 
def calculator(add , sub, mul, div, mod):
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    operator = input("enter operator: ")
    if operator == '+':
        sum = add(a, b)
        print(sum)
    elif operator == '-':
        diff = sub(a, b)
        print(diff)
    elif operator == '*':
        prod = mul(a, b)
        print(prod)
    elif operator == '/':
        divide = div(a, b)
        print(divide)
    elif operator == '%':
        modulus = mod(a, b)
        print(modulus)
    else:
        print("invalid operator")

calculator(add , sub, mul, div, mod)