# 1. swap numbers
a = int(input())
b = int(input())
print(a, b)
a, b = b, a
print(a, b) 

# 2. swap numbers using third variable
x = int(input())
y = int(input())
print(x, y)
temp = x
x = y
y = temp
print(x, y)

# 3. swap numbers without using third variable
c = int(input())
d = int(input())
print(c, d)
c = c + d
d = c - d
c = c - d
print(c, d)