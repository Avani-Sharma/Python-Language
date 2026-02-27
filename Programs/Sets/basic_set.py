# set: is a collection of unique elements which stores the element into the unordered manner 
# it stores the heterogenous elements
# unordered collection 
# set is mutable: after creation we can make changes in it 
# indexing is not possible over the set 
# don't allow duplicate values 

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

# loop
s = {1,2,3,4,5}
for ele in s:
    print(ele)

# print the sum of odd even numbers separetly
s = {1,2,3,4,5}
sum_even =0
sum_odd = 0
for ele in s:
  if ele%2==0:
    sum_even+=ele
  else:
    sum_odd+=ele
print("sum even: ", sum_even)
print("sum odd: ", sum_odd)

# Remove duplicate elements from a list.
li = [1, 2, 3, 2, 4, 1, 5]
unique = []
for i in li:
  if i not in unique:
    unique.append(i)
print(unique)

# remove the duplicate from tuple
t = (1, 2, 3, 4, 3, 5)
key = 3
lst = []
for i in t:
    if i != key:
        lst.append(i)
new_tuple = tuple(lst)
print(new_tuple)

# remove the duplicate characters from the string 'this is python programming class'
s = "this is python programming class"
res = ""
for ch in s:
    if ch not in res:
        res += ch
print(res)

# intersection: finds the common elements between two or more set 
# find common element into the two set
s = {1,2,3,4,5,6}
s1 = {1,2,3,4,2,4}
s2 = {3,4,2,2,4,3,4}
s3 = s.intersection(s1)
s4 = s1 & s2 & s3
print("common elements intersection: ", s3)
print("common elements intersection: ", s4)

# union 
s = {1,2,3,4,5,6}
s1 = {1,2,3,4,2,4}
s2 = {3,4,2,2,4,3,4}
s3 = s.union(s1)
s4 = s1 | s2 | s3
print("common elements union: ", s3)
print("common elements union: ", s4)

# difference
s = {1,2,3,4,5,6}
s1 = {1,2,3,4,2,4}
s2 = s - s1
print("common elements difference: ", s2)

# symmetric difference: (^: XOR operator): remove common elements
s = {1,2,3,4,5,6}
s1 = {4,5,6,7,8}
s2 = s ^ s1
print("common elements symmetric difference: ", s2)

# add one element into the set: use .add()
s = {1,2,3,4}
s.add(5)
print("ADD: ", s)

# add multiple elements into the set: use .update()
s = {1,2,3,4,5,8}
s.update([1,2,45])
print("UPDATE: ", s)

# remove method is used to remove the particular element from the set 
# if that element doesn't present into the set then it would throw an error known as key error

# discard method is used to remove the particualr element from the set if that element 
# which we trying to remove the set not exist into the set then it would not through any error

# pop method is used to remove any element or the random element from the set 

# remove one element from the set: pop(), remove(), discard()
s = {1,2,3,4,5}
s.remove(3)
s.discard(40)
s.pop()
print("REMOVE: " , s)
print("DISCARD: ", s)
print("POP: ", s)