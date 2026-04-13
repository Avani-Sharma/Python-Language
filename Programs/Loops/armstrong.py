n = int(input("enter number: "))
count = 0
sum = 0
temp = n
val = n
while n != 0:
    n = n // 10
    count += 1
while temp != 0:
    d = temp % 10
    sum = sum + (d ** count)
    temp = temp // 10
if sum == val:
    print("armstrong")
else:
    print("not")

# 1-1000 armstrong no.
for n in range(1, 1001):
    count = 0
    sum = 0
    temp = n
    val = n
    while temp != 0:
        temp = temp // 10
        count += 1
    temp = n 
    while temp != 0:
        d = temp % 10
        sum = sum + (d ** count)
        temp = temp // 10
    if sum == val:
        print(n)