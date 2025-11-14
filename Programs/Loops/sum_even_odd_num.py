# sum of even num 1 to 10
sum = 0
for i in range(1, 11):
    if i%2==0:
        sum+=i
print(sum)

# sum of even num while loop
i=1
sum = 0
while i<=10:
    if i%2==0:
        sum +=i
    i+=1
print(sum)

# sum of odd num while loop
sum=0
i = 1
while i<10:
    if i%2!=0:
        sum+=i
    i+=1
print(sum)

# sum of odd num for loop
sum=0
for i in range(1, 11):
    if i%2!=0:
        sum+=i
print(sum)
