# Hollow right triangle
'''
*
* *
*   *
*     *
* * * * *
'''
for i in range(5):
    for j in range(i + 1):
        if j == 0 or j == i or i == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
