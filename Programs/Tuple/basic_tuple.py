# tuple: ordered, immutable, allow duplicate values, heterogeneous elements (means it store multiple 
# items in a single variable).

# uses of tuple
# name of days
# into the database
# colors-> (r, g, b)
# it is faster than list because it is immutable once it create it can't change

# difference between list and tuple
# list is mutable while tuple is immutable
# accessing the elements into the tuple is faster than the list 
# list is initialized with the [] and tuple is initialized with the ()

# since the tuple is immutable in nature, although you want to change the tuple then you have to type cast 
# that tuple tuple into the list then after you can change into the tuple
t = (4,5,6)
print(type(t))
print(t[0])
a = list(t)
a.append(5)
print(a)

print()

# Tuple packing: Tuple packing means putting multiple values into one tuple (bundling them together).
# Many values → one tuple = packing
details = 'avani', 'A26', 21
print(details) 

print()

# tuple unpacking: Tuple unpacking means extracting tuple elements into separate variables.
# One tuple → many variables = unpacking 
details = 'avani', 'A26', 21
name, batch, age = details
print(details)
print(name)
print(batch)
print(age)

print()

# tuple methods: count, index
# count: is used to find the no. of occurence/frequency of elements in the tuple 
# syntax: tuple.count(element)
t = (1,2,3,1,3,2,4,4,5)
print(t.count(2))

print()

# index: is used to find the index of first occurence of the value 
t = (1,2,1,2,1,3,4)
print(t.index(3))

print()

# tuple iterator: through range function 
t = (1,2,3,4)
for i in range(len(t)):
    print(t[i])

print()

# tuple iterator: through membership operator
t = (1,2,3,4)
for ele in t:
    print(ele)

print()


# write a program to seperate even odd numbers from a tuple
t = (1,2,3,4,5,6,7)
even = []
odd = []
for i in t:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even", even)
print("odd", odd)

print()

# write a program to find the largest element from tuple
t = (1,2,4,34,3,5,7,8,9)
max = t[0]
for i in t:
    if i>max:
        max = i
print("Max",max)

print()

# write a program to find the largest element from the even numbers
t = (1,2,3,4,23,5,6,7,8,9)
max = t[0]
for i in t:
    if i%2==0:
        if i>max:
            max = i
print("max", max)

print()

# write a program to find the smallest element from odd numbers
t = (1,2,3,45,6,4,30)
min = t[0]
for i in t:
    if i%2!=0:
        if i<min:
            min = i
print("Min", min)

print()

