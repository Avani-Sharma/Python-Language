# Map function: is also a high order function which maps all the values of iterable with function.
# syntax: map(function, iterable)

li = [1,2,3,4]
result = []
for i in range(len(li)):
    result.append(li[i]**2)
print(result)

# another method 
li = [1, 2, 3, 4]
def sq(x):
    return x**2
print(tuple(map(sq, li)))