# Frozenset: A frozenset is an immutable version of a set in Python.
# Once you create a frozenset, you cannot add or remove elements.
# Just like a normal set, it stores unique elements and supports set operations like union, 
# intersection, difference, and symmetric difference.

# Creating a frozenset
A = frozenset([1, 2, 3, 4])
print(A)

# Set operations
F = frozenset([1, 2, 3])
S2 = {3, 4, 5}
print(F.union(S2)) 
print(F.intersection(S2))

# Use set:  when you need to modify the elements.
# Use frozenset:  when you want an immutable collection or want to use
#  it as a key in a dictionary or inside another set.