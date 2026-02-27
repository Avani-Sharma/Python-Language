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

# find common element into the two set
s = {1,2,3,4,5,6}
s1 = {1,2,3,4,2,4}
s2 = s.intersection(s1)
print("common elements: ", s2)

