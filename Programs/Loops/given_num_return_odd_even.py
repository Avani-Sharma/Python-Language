# take n (123432) input from user and print only odd numbers while loop
n = 123432
while n>0:
    digit = n%10
    if digit%2!=0:
        print(digit)
    n = n//10
print()

# for loop
n = input()
for digit in n:
    if int(digit)%2!=0:
        print(digit)
print()

# even num while loop
n = int(input())
while n>0:
    digit= n%10
    if digit%2==0:
        print(digit)
    n = n//10
print()

# for loop
n = input()
for digit in n:
    if int(digit)%2==0:
        print(digit)


