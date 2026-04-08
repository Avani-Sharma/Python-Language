# inverted centered aligned triangle
print(" Inverted Centered Aligned Triangle Patterns ")

# ques1 
for i in range(4, 0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(4-i+1, end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ques2
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(4-j+1, end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ques3
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ques4
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ques5
num = 1
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(num, end=" ")
            num+=1
        else:
            print(" ", end= " ")
    print()

print()

# ques6
num = 10
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(num, end=" ")
            num-=1
        else:
            print(" ", end=" ")
    print()

print()

# ques7
num = 1
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(num, end=" ")
            num +=2
        else:
            print(" ", end=" ")
    print()

print()

# ques8
num = 19
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(num, end=" ")
            num-=2
        else:
            print(" ", end=" ")
    print()

print()

# ques9
num = 2
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(num, end=" ")
            num+=2
        else:
            print(" ", end=" ")
    print()

print()

# ques10
num = 20
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if j<=i:
            print(num, end=" ")
            num -=2
        else:
            print(" ", end=" ")
    print()

print()