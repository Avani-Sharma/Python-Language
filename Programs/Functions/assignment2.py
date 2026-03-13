# map questions:
# 1 Write a program that takes a list of integers and uses map to return a new list containing the
# square of each number.
li = [1,2,3,4]
def sq(x):
    return x**2
print(list(map(sq, li)))

# 2 Given a list of temperatures in Celsius, use map to convert them into Fahrenheit. 
# (Formula: F = (C × 9/5) + 32)
li = [0, 20, 34, 45]
def convert(C):
    return (C*9/5)+32
print(list(map(convert, li)))

# 3 Take a list of strings and use map to convert each string into its uppercase form.
li = ['avani', 'chinki']
def st(s):
    return s.upper()
print(list(map(st, li)))

# 4 Given a list of numbers, use map with a lambda function to add 10 to each element and print
# the updated list.
li = [10, 20, 30, 40]
result = list(map(lambda a: a+10, li))
print(result)

# 5 Write a program that takes two lists of equal length and uses map to return a list containing the
# sum of corresponding elements.
l1 = [1,2,3,4]
l2 = [5,6,7,8]
def fun(y, z):
    return y+z
result = list(map(fun, l1, l2) )
print(result)


# filter questions: 
# 1 Given a list of integers, use filter to create a new list containing only even numbers.
# 2 Write a program that takes a list of numbers and filters out all numbers greater than 50.
# 3 Given a list of strings, use filter to return only those strings whose length is greater than 5.
# 4 Write a program to filter out all negative numbers from a given list using filter and lambda.
# 5 Given a list of integers, use filter to extract only numbers that are divisible by both 2 and 3.