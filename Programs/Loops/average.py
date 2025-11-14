# calculate average of given n num while loop
n = int(input())
sum=0
count=0
while n>0:
    count+=1
    digit = n%10
    sum +=digit
    n = n//10
print(sum//count)

# for loop
n = input()
sum =0
count=0
for digit in n:
    count+=1
    sum = sum+int(digit)
print(sum/count)
