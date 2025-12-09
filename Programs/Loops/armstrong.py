n = int(input("enter number: "))
count = 0
sum = 0
temp = 0
val = n

while n!=0:
    n = n//10
    count+=1

while temp!=0:
    d = temp%10
    sum = sum + (d**count)
    temp = temp//10

if sum == val:
    print("armstrong")
else:
    print("not")