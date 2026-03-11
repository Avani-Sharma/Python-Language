# filter function: is it a high order function which is used to filter the iterables in which the 
# first argument would be function name second would be iterable name.
# syntax: filter(function, iterable)
# it returns by default a object and we have to convert the filtered object into the list or tuple

li = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2==0, li)))

# ques : write a program to filter out the odd number into the list
li = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2!=0, li)))

# write a program to filter out the odd number into the list
def is_odd(n):
    if n%2!=0:
        return True
    return False
li = [1,2,4,56,78,6]
list(filter(is_odd, li))