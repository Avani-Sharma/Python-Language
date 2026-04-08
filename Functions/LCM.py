def fun(a,b):
    m = max(a,b)
    while True:
        if m%a==0 and m%b==0:
            print("LCM", m)
            break
        m+=1
fun(4,6)