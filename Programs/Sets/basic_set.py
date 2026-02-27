# set: is a collection of unique elements which stores the element into the unordered manner 
# it stores the heterogenous elements
# unordered collection 
# set is mutable: after creation we can make changes in it 

# initialize the set: use {} braces
s = {1,2, 'avani', 1,2}
print(s)
print(type(s))

# we can't initialize empty set with the curly braces
s = {}        # it gives dict 
print(type(s))

# to initialize the empty set: use set constructor
s = set()
print(type(s))

# creating set from list: use set constructor
li = [1,2,3,4]
s = set(li)
print(s)

# in set we store immutable data types
# if we store mutable data type then it gives error : unhashable type: 'list'
s = {1,2, 3,4}
print(s)

# 