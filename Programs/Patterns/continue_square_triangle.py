# continue square triangle
'''
1 2 3 4 
5 6 7 8 
9 10 11 12
13 14 15 16
'''
num = 1
for i in range(1, 5):
    for j in range(1, 5):
        print(num, end=" ")
        num+=1
    print()

print()

'''
16 15 14 13
12 11 10 9
8 7 6 5
4 3 2 1
'''
num = 16
for i in range(1, 5):
    for j in range(1, 5):
        print(num, end=" ")
        num-=1
    print()