# 1 Create a tuple containing five different numbers and display it.
t = (1,2,3,4,5)
print(t)

# 2 Access the first and last element of a tuple.
t = (1,2,3,4,5)
print(t[0])
print(t[-1])

# 3 Find the total number of elements present in a tuple.
t = (1,2,3,4,5)
count = 0
for ele in t:
    count +=1
print(count)

# 4 Check whether a given value exists inside a tuple.
t = (1,2,3,4,5)
if 4 in t:
    print("element exists")
else:
    print("not exists")

# 5 Concatenate two tuples and print the new tuple.
t = (1,2,3,4,5)
t1 = (6,7,8,9)
t2 = t+t1
print(t2)

# 6 Repeat a tuple two times using an operator.
t = (1,2,3,4,5)
t1 = (t) * 2
print(t1)

# 7 Find the index of a specific element in a tuple.
t = (1,2,3,4,5)
t1 = t.index(4)
print(t1)

# 8 Count how many times a particular value appears in a tuple.
t = (1, 2, 3, 2, 4, 2, 5)
val = 2
count = 0
for ele in t:
    if ele == val:
        count += 1
print(count)

# 9 Slice a tuple to display elements from index 1 to 4.
t = (1,2,3,4,5)
t1 = t[1:5]
print(t1)

# 10 Iterate through all elements of a tuple using a loop.
t = (1,2,3,4,5)
for ele in t:
    print(ele)