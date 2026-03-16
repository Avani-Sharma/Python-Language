# print the sum of  1 to n using the recursion.
def add(n):
    if n == 0:
        return 0
    return n + add(n-1)
print(add(5))
    
# another way 
def add(n):
    if n==6:
        return 0
    result = n+add(n+1)
    return result
print(add(1))