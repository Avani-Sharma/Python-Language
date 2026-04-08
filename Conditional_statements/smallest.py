# Accept three numbers and find the smallest among them.

a = int(input())
b = int(input())
c = int(input())
if a<b and a<c:
    print("a is smallest")
elif b<c and b<a:
    print("b is smallest")
else:
    print("c is smallest")