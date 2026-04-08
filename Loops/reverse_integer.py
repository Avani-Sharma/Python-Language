# reverse the digit of number
rev = 0
n = int(input())
sign = -1 if n<0 else 1
n = abs(n)
while n>0:
    digit = n%10
    rev = rev*10+digit
    n = n//10
print(sign*rev)