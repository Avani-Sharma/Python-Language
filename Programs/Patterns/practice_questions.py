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
   *
  * *
 * * *
* * * *
'''
for i in range(1, 5):
    for j in range(4, 0,-1):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(2, 5):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()