# Pyramid of stars
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
for i in range(1, 5):
  for j in range(4, 0, -1):
    if j<=i:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  for j in range(2, i+1):
    print("*", end=" ")
  print()

print()

# inverted pyramid of stars
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
for i in range(4, 0, -1):
  for j in range(4, 0, -1):
    if j<=i:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  for j in range(2, i+1):
    print("*", end=" ")
  print()