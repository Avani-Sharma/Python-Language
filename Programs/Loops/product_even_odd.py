# product of all odd num 1 to 10 using while loop
product = 1
i =1
while i<=10:
    if i%2!=0:
        product*=i
    i+=1
print(product)

# for loop
product =1
for i in range(1, 11):
    if i%2!=0:
        product*=i
print(product)

# product of all even num 1 to 10 using while loop
product =1
i =1
while i<=10:
    if i%2==0:
        product*=i
    i+=1
print(product)

# for loop
product = 1
for i in range(1, 11):
    if i%2==0:
        product*=i
print(product)