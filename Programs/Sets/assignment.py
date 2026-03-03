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

# 11. Given two sets, find their union.
k = {1,2,3,4}
k1 = {3,4,5,6,7}
k2 = k.union(k1)
print("K:", k2)

# 12. Given two sets, find their intersection.
l = {1,2,3,4,5}
l1 = {3,4,5,6,7,8,9}
l2 = l.intersection(l1)
print("L:", l2)

# 13. Find the difference between two sets.
m = {1,2,3,4,5,6,7}
m1 = {1,2,3,4,78,9,8}
m2 = m.difference(m1)
print("M:", m2)

# 14. Find the symmetric difference between two sets.
n = {1,2,3,4,5,7}
n1 = {2,3,4,5,6,7,89,76}
n2 = n.symmetric_difference(n1)
print("N: ", n2)

# 15. Check whether one set is a subset of another.
o = {1,2,3,45}
o1 = {4,1,2,45,5}
o2 = o.issubset(o1)
print("O:", o2)

# 16. Check whether one set is a superset of another.
p = {1,2,3,4}
p1 = {1,2,4,6,7,8}
p2 = p.issuperset(p1)
print("P:", p2)

# 17. Check whether two sets are disjoint.
q = {1,2,3,4}
q1 = {1,2,4,6,7,8}
q2 = q.isdisjoint(q1)
print("Q:", q2)

# 18. Update one set with another set.
r = {1, 2, 3, 4}
r1 = {1, 2, 4, 6, 7, 8}
r.update(r1)  
print("R:", r)

# 19. Remove a random element from a set.
s = {10, 20, 30, 40}
removed = s.pop()
print("S:", removed)

# 20. Find common elements between three sets.
t = {1, 2, 3, 4}
t1 = {2, 3, 5}
t2 = {3, 2, 6}
common = t.intersection(t1, t2)
print("T:", common)

# 21. Given a sentence, find all unique characters using a set.
u = "hello world"
unique_chars = set(u)
print("U:", unique_chars)

# 22. Count the number of unique words in a paragraph using a set.
v = "python is easy and python is fun"
words = v.split()
unique_words = set(words)
print("V:", len(unique_words))

# 23. Given two lists, return a list of common unique elements using sets.
w = [1, 2, 2, 3, 4]
w1 = [2, 3, 5, 6]
common = list(set(w) & set(w1))
print("W:", common)

# 24. Find elements that appear in either of the two sets but not in both.
x = {1, 2, 3, 4}
x1 = {3, 4, 5, 6}
x2 = x.symmetric_difference(x1)
print("X:", x2)

# 25. Given a list of numbers, find all duplicate elements using sets.
y = [1, 2, 3, 2, 4, 5, 1, 6]
seen = set()
duplicates = set()
for num in y:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("Y:", duplicates)

# 26. Write a program to check if two strings are anagrams using sets.
z = "listen"
z1 = "silent"
print(set(z) == set(z1))

# 27. Given a set of numbers, remove all even numbers.
s = {1, 2, 3, 4, 5, 6}
s = {x for x in s if x % 2 != 0}
print("remove even:", s)

# 28. Create a set comprehension to generate squares of numbers from 1 to 10.
squares = {x*x for x in range(1, 11)}
print("Squares:", squares)

# 29. From a given set, create a new set containing only numbers greater than 10.
s = {5, 12, 7, 18, 3, 25}
new_set = {x for x in s if x > 10}
print("Set:", new_set)

# 30. Given multiple sets in a list, find the intersection of all sets.
sets_list = [{1,2,3,4}, {2,3,5}, {2,3,6}]
result = set.intersection(*sets_list)
print("intersection:", result)