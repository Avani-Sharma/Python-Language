# ques1
for i in range(1, 5):
    for j in range(1, 5):
        if (i==4 or i==j or j==1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ques2
for i in range(4, 0, -1):
    for j in range(1, 5):
        if (i==4 or i==j or j==1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ques3
for i in range(1, 5):
    for j in range(4, 0, -1):
        if (i==4 or i==j or j==1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ques4
for i in range(4, 0, -1):
    for j in range(4, 0, -1):
        if (i==4 or i==j or j==1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()