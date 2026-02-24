# list comprehension: it is a concised way to generate a list by using for loop and some condition
# syntax: [expression for expression in range() some condition]

# Create a list of numbers from 1 to 10 using list comprehension.
num = [X for X in range(1,11)]
print("A:", num)
print()

# generate the square of all the numbers from 1 to 10
num = [X*X for X in range(1, 11)]
print("B:", num)
print()

# Create a list containing cubes of numbers from 1 to 10.
num = [X*X*X for X in range(1, 11)]
print("C:", num)
print()

# generate a list of even numbers from 1 to 20
num = [X for X in range(1,21) if X% 2==0]
print("D:", num)
print()

# generate a list of odd numbers from 1 to 20
num = [X for X in range(1, 20) if X%2 !=0]
print("E:", num)
print()

# Create a list of numbers divisible by 3 from 1 to 30.
num = [X for X in range(1, 30) if X%3 ==0]
print("F:", num)
print()

# Create a list of numbers greater than 10 from a given list.
li1 = [1,2,4,6,7,8,9,10,12,14]
li1 = [X for X in li1 if X>10]
print("G:", li1)
print()

# From a list of numbers, create a new list containing only positive numbers.
li = [-5, 3, -2, 7, 0, 9, -1]
pos = [x for x in li if x > 0]
print("H:", pos)
print()

# From a list, create a list containing only negative numbers.
li = [-5, 3, -2, 7, 0, 9, -1]
pos = [x for x in li if x < 0]
print("I:", pos)
print()

# Create a list of numbers whose square is greater than 50.
num = [X*X for X in range(1, 11) if X*X>50]
print("J:", num)
print()

# Convert all words of a list into uppercase using list comprehension.
li = ['apple', 'car', 'elephant', 'dog', 'cat']
upper_words = [word.upper() for word in li]
print("Upper:", upper_words)
print()

# Convert all words into lowercase.
li = ['apple', 'car', 'elephant', 'dog', 'cat']
lower_words = [word.lower() for word in li]
print("Lower:", lower_words)
print()

# Create a list containing length of each word from a list of strings.
li = ['apple', 'car', 'elephant', 'dog', 'cat']
lengths = [len(word) for word in li]
print("Lengths:", lengths)
print()

# Extract only words having more than 4 characters.
li = ['apple', 'car', 'elephant', 'dog', 'cat']
li = [word for word in li if len(word) > 4]
print("N:", li)
print()

# generate a list from 100 to 1
num = [X for X in range(100, 0, -1)]
print("O:", num)
print()

# generate a list of words which has length less than 4
li = ['apple', 'car', 'elephant', 'dog', 'cat']
li = [word for word in li if len(word) < 4]
print("P:", li)
print()

# generate a list of odd numbers from 100 to 1
num = [X for X in range(100, 0, -1) if X%2 !=0]
print("Q:", num)