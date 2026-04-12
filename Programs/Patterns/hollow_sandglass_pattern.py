# hollow sandglass pattern
for i in range(4, 0, -1):
  for j in range(4, 0, -1):
    if i==j or i==4:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  for j in range(2, i+1):
    if i==j or i==4:
        print("*", end=" ")
    else:
        print(" ", end=" ")
  print()
for i in range(2, 5):
  for j in range(4, 0, -1):
    if i==j or i==4 :
      print("*", end=" ")
    else:
      print(" ", end=" ")
  for j in range(2, i+1):
    if i==j or i==4 :
        print("*", end=" ")
    else:
        print(" ", end=" ")
  print()