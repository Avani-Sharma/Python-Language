# list comprehension: it is a concised way to generate a list by using for loop and some condition
# syntax: [expression for expression in range() some condition]

# generate a list from 1 to 100
num = [X for X in range(1,101)]
print(num)

# generate a list from 100 to 1
num = [X for X in range(100, 0, -1)]
print(num)
print()

# generate a list of even numbers from 1 to 100
num = [X for X in range(1,101) if X% 2==0]
print(num)
print()

# generate a list of odd numbers from 1 to 100
num = [X for X in range(1, 100) if X%2 !=0]
print(num)
print()

# generate the square of all the numbers from 1 to 10
num = [X*X for X in range(1, 11)]
print(num)
print()

# generate a list of words which has length less than 4
li = ['apple', 'car', 'elephant', 'dog', 'cat']
li = [word for word in li if len(word) < 4]
print(li)
print()

# generate a new list which has numbers greater than 10
li1 = [1,2,4,6,7,8,9,10,12,14]
li1 = [X for X in li1 if X>10]
print(li1)
print()

# generate a list of odd numbers from 100 to 1
num = [X for X in range(100, 0, -1) if X%2 !=0]
print(num)