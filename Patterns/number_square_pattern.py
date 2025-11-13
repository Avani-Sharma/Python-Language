# number square pattern  
'''
1 1 1 1 
1 1 1 1 
1 1 1 1 
1 1 1 1 
'''
for i in range(1, 5):
    for j in range(1, 5):
        print("1", end=" ")
    print()

print()

'''
1 2 3 4 
1 2 3 4
1 2 3 4
1 2 3 4
'''
for i in range(1, 5):
    for  j in range(1, 5):
        print(j, end=" ")
    print()

print()

'''
1 1 1 1
2 2 2 2 
3 3 3 3 
4 4 4 4
'''
for i in range(1, 5):
    for j in range(1, 5):
        print(i, end=" ")
    print()

print()

'''
4 3 2 1
4 3 2 1
4 3 2 1
4 3 2 1
'''
for i in range(4, 0, -1):
    for j in range(4, 0, -1):
        print(j, end=" ")
    print()

print()

'''
4 4 4 4
3 3 3 3
2 2 2 2 
1 1 1 1
'''
for i in range(4, 0, -1):
    for j in range(4, 0, -1):
        print(i, end=" ")
    print()