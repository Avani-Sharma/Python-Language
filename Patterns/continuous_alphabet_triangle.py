# Continuous alphabet triangle
'''
A
B C
D E F
G H I J
'''
ch = 65  
for i in range(1, 5):  
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
