# sum of given prime num while loop
n = int(input())
sum =0
while n>0:
    digit = n%10
    if(digit==2 or digit==3 or digit==5 or digit==7):
        sum+=digit
    n = n//10
print(sum) 

# sum of given prime num for loop
n = input()
sum = 0
for digit in n:
    d = int(digit)
    if(d==2 or d==3 or d==5 or d==7):
        sum +=d
print(sum)