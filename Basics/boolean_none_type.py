# 1. Print the boolean value of 0, 1, and -5.
a = 0
b = 1
c = -5
print(bool(a))
print(bool(b))
print(bool(c))

# 2. Print the boolean value of an empty string "" and a non-empty string "Hello".
d = ""
e = "hello"
print(bool(d))
print(bool(e))

# 3. Assign None to a variable and print it along with its type.
f = None 
print(f)
print(type(f))

# 4. Check what bool(None) returns and explain why.
# None represents "no value" so it boolean value is False
g = bool(None)
print(g) 

# 5. Write a program that checks if an input string is empty or not using bool().
h = input("")
print(bool(h))

# 6. What is the result of bool("") and bool("Python")
x = bool("")
y = bool("python")
print(x)
print(y)

# 7. What is the type of the output of this expression: 3 + 4.0
m = 3 + 4.0
print(type(m))

# 8. What will be printed by this code: n = None\nprint(bool(n))
n = None
print(bool(n))