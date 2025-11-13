#  Right-angled triangle
'''
*
* *
* * *
* * * *
* * * * *
'''
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
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
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
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
rows = 5
for i in range(1, rows + 1):  
    for j in range(1, rows + 1):  
        if j <= rows - i:
            print("  ", end="")  
        else:
            print("* ", end="")  
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
rows = 5
for i in range(rows, 0, -1):  
    for j in range(rows - i):
        print("  ", end="")  
    for k in range(i):
        print("* ", end="")   
    print()
