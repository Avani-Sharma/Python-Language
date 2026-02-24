#  Right-angled triangle
'''
*
* *
* * *
* * * *
* * * * *
'''
for i in range(1, 5):
    for j in range(1, 5):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# Inverted right-angled triangle
'''
* * * * *
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

# centered aligned triangle
'''
        *
      * *
    * * * 
  * * * *
* * * * *
'''
for i in range(1, 5):
    for j in range(4, 0, -1):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# inverted centered aligned triangle
'''
* * * * *
  * * * *
    * * *
      * * 
        *
'''
for i in range(4, 0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()