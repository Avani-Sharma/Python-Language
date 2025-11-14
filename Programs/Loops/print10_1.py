# Print numbers from 10 down to 1 (reverse order).
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# take input from user n for loop
n = int(input("enter n: "))
for i in range(10, n, -1):
    print(i, end=" ")
print()

# print number 10 to 1 using while loop
i = 10
while i>=1:
    print(i, end=" ")
    i = i-1
print()

# take input from  user n while loop
n = int(input("enter n: "))
i=10
while i>=n:
    print(i, end=" ")
    i = i-1

