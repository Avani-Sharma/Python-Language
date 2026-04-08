# Number pyramid
'''
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''
for i in range(1, 6):
  for j in range(5, 0, -1):
    if j<=i:
      print(i-j+1, end=" ")
    else:
      print(" ", end=" ")
  for j in range(2, i+1):
    print(i-j+1, end=" ")
  print()
