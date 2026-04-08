# minimum number take input from user while loop
n = int(input())
min = 9
while n>0:
    digit = n%10
    if digit<min:
        min = digit
    n = n//10
print(min)

# minimum number take input from user for loop
n = input()
min = 9
for i in n:
    d = int(i)
    if d<min:
        min = d
print(min)