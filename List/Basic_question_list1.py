# 1 Create a list of 5 integers and print it.
a = [1,2,3,4,5]
print("A: ", a)

# 2 Create a list of 3 different data types and print each element.
b = [1, 'avani', True]
print("B: " , b)

# 3 Create an empty list and add three elements to it.
c =[]
c.extend([1,2,3])
print("C: ", c)

# 4 Create a list of 6 numbers and print the first element.
d = [1,2,3,4,5,6]
print("D: ", d[0])

# 5 Print the last element of a list using negative indexing.
e = [1,2,3,4,5,6]
print("E: ", e[-1])

# 6 Given a list, print the third element.
f = [1,2,3,4,5]
print("F: ", f[2])

# 7 Extract the first three elements using slicing.
g = [1,2,3,4,5,6,7]
print("G: ", g[0:3])

# 8 Reverse a list using slicing.
h = [1,2,3,4,5,6]
print("H: ", h[::-1])

# 9 Create a list and change the second element to a new value.
i = [1,2,3,4,5]
i[1] = 33
print("I: ", i)

# 10 Replace the last element of a list with 100.
j = [1,2,3,4,5]
j[-1] = 100
print("J: ", j)

# 11 Modify multiple elements in a list using slicing.
k = [1,2,3,4,5]
k[1:3] = [100,200]
print("K: ", k)

# 12 Create a list and use append() to add one element.
l = [1,3,4,7,5,6]
l.append(9)
print("L: ", l)

# 13 Use extend() to add multiple elements to a list.
m = [1,2,3,4,5,6,7]
m.extend([3,4,5])
print("M: ", m)

# 14 Use insert() to add an element at index position 2.
n = [1,2,3,4,5,7]
n.insert(2, 89)
print("N: ", n)

# 15 Remove an element using remove().
o = [1,2,3,4,5]
o.remove(4)
print("O: ", o)

# 16 Remove an element using pop() and print the removed value.
p = [1,2,4,55]
removed = p.pop(2)
print("removed: ", removed)
print("P: ", p)

# 17 Clear all elements from a list.
q = [1,2,34,4]
q.clear()
print("Q: ", q)

# 18 Print all elements of a list using a for loop.
r = [1,2,34,5,7]
for i in range(len(r)):
    print("R: ",r[i])

# 19 Print only even numbers from a list using a loop.
s = [1,2,3,4,5]
li = []
for ele in s:
    if ele %2 == 0:
        li.append(ele)
print("S: ", li)

# 20 Count how many numbers are greater than 10 using a loop.
t = [1,2,4,5,6,67,46,6,42]
li = []
for ele in t:
    if ele >10:
        li.append(ele)
print("T: ", li)

# 21 Find the sum of all elements in a list using a loop.
u = [1,2,4,5,6,67,46,6,42]
sum = 0
for i in range(len(u)):
    sum += u[i]
print("U: ", sum)

# 22 Find the maximum element in a list without using max().
v = [1,2,4,5,6]
max = v[0]
for ele in v:
    if ele > max:
        max= ele
print("V: ", max)