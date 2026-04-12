# Reverse a number using a while loop (e.g., 123 should become 321).

num = int(input())
rev = 0
while num>0:
    digit = num%10
    rev = rev * 10 + digit
    num = num//10
print(rev)

# for loop
n = input()
rev = ""
for i in n:
    rev = i+rev
print(rev)
