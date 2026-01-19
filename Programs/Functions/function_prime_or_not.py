# write a program to check whether a number is prime or not

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
check_prime = is_prime(7)
if check_prime:
    print("number is prime")
else:
    print("number is not prime")