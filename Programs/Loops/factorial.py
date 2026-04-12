# Find the factorial of a given number using a loop.

n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("Factorial of", n, "is:", fact)
