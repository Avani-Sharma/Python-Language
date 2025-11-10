# 1. input num as a string. You need to typecast into an integer and double it. 
num = input()
print(int(num)*2)

# 2. Convert an integer a = 10 to float, string, and bool — print all.
a = 10 
print(a)
print(float(a))
print(str(a))
print(bool(a))

# 3. Convert a string "123" into integer and float and print both results.
s ="123"
print(int(s))
print(float(s))

# 4. Convert 0 and 1 into boolean and print the results.
x = 0
y = 1
print(bool(x))
print(bool(y))

# 5. Convert a float value 3.14 into int and print the result.
pi = 3.14
print(int(pi))

# 6. Convert True and False into integers and print both.
b = True
c = False 
print(int(b))
print(int(c))

# 7. two string inputs, converts them to integers, and performs addition, subtraction, multiplication, and division
# Print all results and show the types before and after conversion.
a = input("Enter first number: ")
b = input("Enter second number: ")
print("Before conversion:")
print("Type of a:", type(a))
print("Type of b:", type(b))
a = int(a)
b = int(b)
print("After conversion:")
print("Type of a:", type(a))
print("Type of b:", type(b))
add = a + b
sub = a - b
mul = a * b
div = a / b
print(add, sub, mul, div)
