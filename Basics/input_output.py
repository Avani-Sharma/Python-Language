# 1. Take a number as input and print its type before and after converting it to int.
a = input("enter a number: ")
print(type(a))
print(type(int(a)))

# 2. Take two numbers as input and print their sum (after type casting).
b = input("enter b: ")
c = input("enter c: ")
print(int(b)+int(c))

# 3. Take a user’s name as input and print a greeting message using string concatenation.
name = input("enter name: ")
print("Good Morning, " + name)

# 4. Take one input and print its boolean value using the bool() function.
d = input("enter d: ")
print(bool(d))

# 5. Take two inputs and print the result of multiplying them after converting to integers.
x = input("enter x: ")
y = input("enter y: ")
print(int(x)*int(y))