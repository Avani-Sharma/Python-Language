# Sandglass pattern
'''
* * * * *
  * * * *
    * * *
      * *
        *
      * *
    * * *
  * * * *
* * * * *
'''
rows = 5
for i in range(rows, 0, -1):  
    for j in range(rows - i):
        print("  ", end="")  
    for k in range(i):
        print("* ", end="")   
    print()
rows = 5
for i in range(2, rows + 1):  
    for j in range(1, rows + 1):  
        if j <= rows - i:
            print("  ", end="")  
        else:
            print("* ", end="")  
    print()

