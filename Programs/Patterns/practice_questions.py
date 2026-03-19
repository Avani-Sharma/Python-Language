'''
* * * *
* * * *
* * * *
* * * *
'''
for i in range(1, 5):
    for j in range(1, 5):
        print("*", end=" ")
    print()

print()

'''
*
* *
* * *
* * * *
'''
for i in range(1, 5):
    for j in range(1, 5):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

'''
* * * *
* * *
* *
*
'''
for i in range(4, 0, -1):
    for j in range(1, 5):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

'''
1
1 2
1 2 3
1 2 3 4
'''
for i in range(1, 5):
    for j in range(1, 5):
        if j<=i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

print()

'''
1
2 2
3 3 3
4 4 4 4
'''
for i in range(1, 5):
    for j in range(1, 5):
        if j<=i:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()

print()

'''
1
2 3
4 5 6
7 8 9 10
'''
num = 1
for i in range(1, 5):
    for j in range(1, 5):
        if j<=i:
            print(num, end=" ")
            num+=1
        else:
            print(" ", end=" ")
    print()

print()

'''
A
A B
A B C
A B C D
'''
for i in range(1, 5):
    ch = 'A'
    for j in range(1, 5):
        if j<=i:
            print(ch, end=" ")
            ch = chr(ord(ch)+1)
        else:
            print(" ", end=" ")
    print()

print()

'''
A
B B
C C C
D D D D
'''
ch = 'A'
for i in range(1, 5):
    for j in range(1, 5):
        if j<=i:
            print(ch, end=" ")
        else:
            print(" ", end=" ")
    ch = chr(ord(ch)+1)
    print()

'''
*       *
  *   *
    *
  *   *
*       *
'''
for i in range(1, 4):
    for j in range(1, 4):
        if j==i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(2, 0, -1):
        if j==i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(2, 0, -1):
    for j in range(1, 4):
        if j==i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(2, 0, -1):
        if j==i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()