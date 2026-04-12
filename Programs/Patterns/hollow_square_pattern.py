# ques1
for i  in range(1, 5):
    for j in range(1, 5):
        if (i==1 or i==4 or j==1 or j==4):
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ques2
for i  in range(1, 5):
    for j in range(1, 5):
        if (i==1 or i==4 or j==1 or j==4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# ques3
for i  in range(1, 5):
    ch = 'A'
    for j in range(1, 5):
        if (i==1 or i==4 or j==1 or j==4):
            print(ch, end=" ")
        else:
            print(" ", end=" ")
        ch = chr(ord(ch)+1)
    print()