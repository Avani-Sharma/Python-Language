# Map function: is used to map all the elements of the iterables with a function 
# syntax: map(function, iterable)

def square(n):
    return n*n
li = [1, 2, 3, 4]
mapped_obj=list(map(square,li))
mapped_obj1 = list(map(lambda n:n*n,li))
print(mapped_obj)
print(mapped_obj1) 