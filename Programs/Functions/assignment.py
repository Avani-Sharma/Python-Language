# 1 Write a function that takes two numbers as input and returns their sum.
def fun(a, b):
    return a+b
result = fun(4,5)
print("sum: ", result)

# 2 Write a function that takes a number and returns its square.
def fun(n):
    return n*n
result = fun(5)
print("square: ", result)

# 3 Write a function that takes a number and returns its cube.
def fun(m):
    return m*m*m
result = fun(5)
print("cube: ", result)

# 4 Write a function that takes a number and returns whether it is even or odd.
def fun(s):
    if s%2==0:
        return "even"
    else:
        return "odd"
result = fun(100)
print("even/odd: ", result )

# 5 Write a function that takes a number and returns its factorial.
def fun(o):
    fact = 1
    while o>1:
        fact*=o
        o-=1
    return fact
result = fun(5)
print("factorial: ", result)

# 6 Write a function that takes two numbers and returns the larger number.
def fun(c, d):
    if c>d:
        return c
    else:
        return d
result = fun(4, 5)
print("larger no.: ", result )
    
# 7 Write a function that takes three numbers and returns the smallest number.
def fun(e, f, g):
    if e<f and e<g:
        return e
    elif f<e and f<g:
        return f
    else:
        return g
result = fun(4, 5, 9)
print("smallest no.: ", result )

# 8 Write a function that takes a number and returns the reverse of the number.
def fun(h):
    rev = 0
    while h!=0:
        digit = h%10
        rev = rev*10+digit
        h= h//10
    return rev
result = fun(123)
print("reverse: ", result)

# 9 Write a function that takes a number and returns the sum of its digits.
def fun(i):
    sum = 0
    while i>0:
        digit = i%10
        sum = sum+digit
        i = i//10
    return sum
result = fun(345)
print("sum of its digit: ", result)

# 10 Write a function that takes a number and returns whether it is a palindrome or not.
def fun(j):
    rev = 0
    temp =j
    while j!=0:
        digit = j%10
        rev = rev*10+digit
        j = j//10
    if temp == rev:
        return "palindrome"
    else:
        return "not palindrome"
result = fun(121)
print("palindrome or not: ", result)

# 11 Write a function that takes a number and returns the count of digits in the number.
def fun(k):
    count = 0
    while k!=0:
        count+=1
        k = k//10
    return count
result = fun(1234)
print("count: ", result)

# 12 Write a function that takes a number and returns whether it is a prime number or not.
def fun(l):
    count = 0
    for i in range(1, l+1):
        if l%i == 0:
            count+=1
    if count == 2:
        return "prime"
    else:
        return "not prime"
result = fun(12)
print("prime or not: ", result)

# 13 Write a function that takes two numbers and returns their product.
def fun(p,q):
    return p*q
result = fun(4,5)
print("product: ", result)

# 14 Write a function that takes two numbers and returns the remainder when the first number is
# divided by the second.
def fun(r, t):
    remainder = r%t
    return remainder
result = fun(10, 3)
print("remainder: ", result)

# 15 Write a function that takes a number and returns the sum of numbers from 1 to that number.
def fun(u):
    sum = 0
    for i in range(1, u+1):
        sum = sum+i
    return sum
result = fun(10)
print("sum: ", result)

# 16 Write a function that takes a number and returns the multiplication table of that number.
def fun(w):
    for i in range(1, 11):
        print(w , "x" , i, "=", w*i)
fun(5)

# 17 Write a function that takes two numbers and returns the power of the first number raised to the
# second number.
def fun(y,z):
    return y ** z
result = fun(2,3)
print("power: ", result)

# 18 Write a function that takes a number and returns the last digit of the number.
def last_digit(n):
    return n % 10
result = last_digit(1234)
print("last digit: ", result)

# 19 Write a function that takes a number and returns the first digit of the number.
def first_digit(n):
    while n >= 10:
        n = n // 10
    return n
result = first_digit(5678)
print("first digit: ", result)

# 20 Write a function that takes two numbers and returns the absolute difference between them.
def absolute_difference(a, b):
    return abs(a - b)
result = absolute_difference(10, 4)
print("absolute difference: ", result)