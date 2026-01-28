# filter 
# syntax: filter(function, iterable)
li = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2==0, li)))

# ques : write a program to filter out the odd number into the list
li = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2!=0, li)))