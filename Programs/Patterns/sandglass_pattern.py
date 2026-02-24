# sandglass pattern 
for i in range(4, 0, -1):
  for j in range(4, 0, -1):
    if j<=i:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  for j in range(2, i+1):
    print("*", end=" ")
  print()
for i in range(2, 5):
  for j in range(4, 0, -1):
    if j<=i:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  for j in range(2, i+1):
    print("*", end=" ")
  print()

print()

# half left sandglass pattern
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
for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(2, 6):
    for j in range(5, 0, -1):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# half right sandglass pattern
for i in range(4, 0, -1):
    for j in range(1, 5):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(2, 5):
    for j in range(1, 5):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()