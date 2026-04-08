# find maximum num in a given num
n = int(input())
max =0
while n>0:
    digit = n%10
    if digit>max:
        max=digit
    n = n//10
print(max)

# for loop
n = input()
max =0
for i in n:
    d = int(i)
    if d>max:
        max = d
print(max)