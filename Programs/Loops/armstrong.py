n = int(input())
temp= n
sum = 0
while n>0:
    d = n%10
    sum=sum+(d*d*d)
    n = n//10
if temp == sum:
    print("armstrong")
else:
    print("not armstrong")