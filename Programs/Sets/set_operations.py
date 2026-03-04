# Union → | or union(): Combines all unique elements from two sets.
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)          
print(A.union(B)) 

# Intersection → & or intersection(): Gives only the common elements between two sets.
A = {1, 2, 3}
B = {2, 3, 4}
print(A & B)             
print(A.intersection(B))

# Difference → - or difference(): Gives elements of one set that are not present in the other set.
A = {1, 2, 3}
B = {2, 3, 4}
print(A - B)  
print(B - A)

# Symmetric Difference → ^ or symmetric_difference(): Gives elements that are in either set, 
# but not in both (removes common elements).
A = {1, 2, 3}
B = {2, 3, 4}
print(A ^ B)                  
print(A.symmetric_difference(B))

# isdisjoint() → Returns True if no common elements between A and B otherwise False
A = {1, 2, 3}
B = {4, 5, 6}
C = {3, 4}
print(A.isdisjoint(B)) 
print(A.isdisjoint(C))

# issubset() → Returns True if all elements of A are in B
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))
print(B.issubset(A))

# issuperset() → Returns True if A contains all elements of B
A = {1, 2, 3, 4}
B = {2, 3}
print(A.issuperset(B))  
print(B.issuperset(A))