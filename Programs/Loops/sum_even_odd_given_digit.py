# sum of even digit in a given number
sum=0
n = int(input())
while n>0:
    digit = n%10
    if digit%2==0:
        sum +=digit
    n = n//10
print(sum)

# for loop
sum = 0
n = input()
for digit in n:
    d = int(digit)       # convert to int
    if d%2!=0:
        sum +=d
print(sum)

# sum of odd digit in a given number
sum = 0
n = int(input())
while n>0:
    digit = n%10
    if digit%2!=0:
        sum+=digit
    n = n//10
print(sum)

# for loop
sum=0
n = input()
for digit in n:
    d = int(digit)
    if d%2==0:
        sum+=d
print(sum)
