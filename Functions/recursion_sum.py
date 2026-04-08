#  write a program to ptint the sum of the 1 to 10 using recursion
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)
print(sum_numbers(10))

# recursion work on lifo concept = last in first out

print()

# print the sum of all the digits of a number using recursion
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)
print(sum_digits(123))