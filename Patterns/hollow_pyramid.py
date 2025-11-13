# Hollow pyramid
'''
        *
      *   *
    *       *
  *           *
* * * * * * * * *
'''
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows * 2):
        if j <= rows - i or j >= rows + i:
            print(" ", end=" ")
        elif j == rows - i + 1 or j == rows + i - 1 or i == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
