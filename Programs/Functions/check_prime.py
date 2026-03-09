# write a function to check whether a number is prime or not
def is_prime(n):
    fact = 0
    for i in range(1, n+1):
        if n%i == 0:
            fact+=1
    if fact == 2:
        return True
    else:
        return False
is_prime = is_prime(8)
if is_prime:
    print("prime")
else:
    print("not prime")

# print all the prime numbers from 2 to 100 using the function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for i in range(2, 101):
    if is_prime(i):
        print(i, end=" ")
