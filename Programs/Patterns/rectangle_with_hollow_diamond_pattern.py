# rectangle with hollow diamond pattern
for i in range(4, 0, -1):
    for j in range(1, 5):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(4, 0, -1):
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
    for j in range(4, 0, -1):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()