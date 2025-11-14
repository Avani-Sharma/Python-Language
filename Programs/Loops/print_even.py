# print all even numbers between 1 and 10
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# input from user and print all even number between 1 to 10(n) for loop
n = int(input("enter n: "))
for i in range(2, n, 2):
    print(i, end=" ")
print()

# reverse for loop print even num 10 to 1 
for i in range(10, 1, -2):
    print(i, end=" ")
print()

#using while loop
i=2
while i<=10:
    print(i, end=" ")
    i+=2
print()

# input from user and print all even number between 1 to 10(n) while loop
n = int(input("enter n: "))
i = 2
while i<=n:
    print(i, end=" ")
    i+=2
print()

# reverse while loop print num 10 to 1
i = 10
while i>=1:
    print(i, end=" ")
    i-=2