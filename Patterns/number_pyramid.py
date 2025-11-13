# Number pyramid
'''
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''
rows = 5
for i in range(1, rows + 1):
    num = 1  
    for j in range(1, rows * 2):  
        if j >= rows - (i - 1) and j <= rows + (i - 1):
            print(num, end=" ")
            if j < rows:  
                num += 1
            else:  
                num -= 1
        else:
            print(" ", end=" ")
    print()
