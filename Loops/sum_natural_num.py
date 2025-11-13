# Calculate and print the sum of the first 10 natural numbers (i.e., 1 + 2 + ... +10).

sum = 0
for i in range(1,11):
    sum += i
print(sum)

#  while loop
sum = 0
i = 1
while i <= 10:
    sum += i    
    i += 1
print("Sum of first 10 natural numbers is:", sum)

# take n input from user and sum upto n numbers
n = int(input())
sum = 0
for i in range(1, n):
    sum+=i
print(sum)

# take n input from user and sum upto n number while loop
n = int(input())
sum = 0
i = 1
while i<=n:
    sum +=i
    i +=1
print(sum)

# reverse order sum 10 to 1 using for loop
sum = 0
for i in range(10, 0, -1):
    sum+=i
print(sum)

# reverse in while loop and sum
sum = 0
i=10
while i>=1:
    sum +=i
    i  -=1
print(sum)