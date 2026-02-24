# hollow diamond 
for i in range(1, 5):
  for j in range(4, 0, -1):
    if i==j  :
      print("*", end=" ")
    else:
      print(" ", end=" ")
  for j in range(2, i+1):
    if i==j :
        print("*", end=" ")
    else:
        print(" ", end=" ")
  print()

for i in range(3, 0, -1):
  for j in range(4, 0, -1):
    if i==j :
      print("*", end=" ")
    else:
      print(" ", end=" ")
  for j in range(2, i+1):
    if i==j :
        print("*", end=" ")
    else:
        print(" ", end=" ")
  print()