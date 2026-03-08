x = -123
sign = 1
if x<0:
    sign = -1
    x = -x

rev = 0
while x>0:
    digit = x%10
    rev = rev*10+digit
    x = x//10

rev = sign*rev

if rev< -2**31 or rev>2**31 -1:
    print(0)
else:
    print(rev)