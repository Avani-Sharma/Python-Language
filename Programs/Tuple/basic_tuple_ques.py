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

# Tuple packing:  is the process of grouping multiple values into a single tuple object in Python. 
# This is an automatic feature of Python that occurs whenever multiple comma-separated values are 
# assigned to a single variable. Parentheses are optional but are often used for clarity.
details = 'avani', 'A26', 21
# here grouping multiple values into the single variable and this process is known as tuple packing
print(details) 