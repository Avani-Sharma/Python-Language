a = int(input())
b = int(input())
m = max(a, b)
while True:
    if m%a==0 and m%b==0:
        print("LCM", m)
        break
    m+=1