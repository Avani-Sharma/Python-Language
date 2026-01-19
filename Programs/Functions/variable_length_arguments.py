# variable length arguments: are used to pass the variable length of the arguments,
# either it could two or more
# it return all the arguments in the form of tuple 

def add(*args):
    sum = 1
    for element in args:
        sum += element
    return sum
print(add(2,3,4,6,4,7,8))

# 