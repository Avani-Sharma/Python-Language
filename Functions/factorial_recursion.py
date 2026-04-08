# print the factorial using the recursion ->5
def sum_numbers(n):
    if n == 1:
        return 1
    return n * sum_numbers(n - 1)

print(sum_numbers(5))