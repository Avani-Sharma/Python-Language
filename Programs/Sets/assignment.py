# 1. create a set of numbers from 1 to 5 and print it.
a = {1,'avani', 3, 4.7, 2}
print("A: ", a)

# 2. add an element to an existing set.
b = {1,2,3,4}
b.add(6)
print("B: ", b)

# 3. remove an element using remove().
c = {1,2,3,4,5}
c.remove(1)
print("C: ", c)

# 4. remove an element using discard().
d = {1,2,3,4,5}
result = d.discard(50)
print("D: ", result)

# 5. find the length of set
e = {1,2,3,5,6,7,9}
print("E: ", len(e))

# 6. check if element exist in a set
f = {1,2,3,4,5}
found = False
for ele in f:
    if ele == 4:
        found = True
        break
print("F:", ele)

# 7. Clear all elements from a set.
g = {1,2,3,4,5}
g.clear()
print("G:", g)

# 8. Convert a list with duplicate values into a set to remove duplicates.
h = [1,3,2,3,4,2,4]
unique_set = set(h)
print("H:", unique_set)

# 9. Create an empty set correctly (without using {}).
i = set()
print("I:", type(i))

# 10. Iterate through a set and print each element.
j = {1,2,3,4,5}
for ele in j:
    print("J:", ele)