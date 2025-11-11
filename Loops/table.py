# Take a number n and print its full multiplication table (up to 10 multiples).

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1
