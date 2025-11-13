# print all odd numbers between 1 and 10
for i in range(1, 10, 2):
    print(i, end=" ")
print()

# input from user and print all odd number between 1 to 10(n) for loop
n = int(input("enter n: "))
for i in range(1, n, 2):
    print(i, end=" ")
print()

# reverse odd numbers 10 to 1 for loop
for i in range(9, 0, -2):
    print(i, end=" ")
print()

#using while loop
i=1
while i<=10:
    print(i, end=" ")
    i+=2
print()

# input from user and print all odd number between 1 to 10(n) while loop
n = int(input("enter n: "))
i = 1 
while i<=n:
    print(i, end=" ")
    i+=2
print()

#reverse odd num 10 to 1 while loop
i = 9
while i>=1:
    print(i, end=" ")
    i-=2