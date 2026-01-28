#  print the numbers from 1 to 10 using the recursion
def print_numbers(n):
    if n == 11:
      return
    print(n)
    print_numbers(n + 1)
print_numbers(1)

print()

#  print the numbers from 10 to 1 using the recursion
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)
print_numbers(10)