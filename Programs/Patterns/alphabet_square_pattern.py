# ques1
for i in range(1, 5):
    ch = 'A'
    for j in range(1, 5):
        print(ch, end=" ")
        ch = chr(ord(ch)+1)
    print()

print()

# ques2
ch = 'A'
for i in range(1, 5):
    for j in range(1, 5):
        print(ch, end=" ")
    print()
    ch = chr(ord(ch)+1)

print()

# ques3
ch = 'A'
for i in range(1, 5):
    for j in range(1, 5):
        print(ch, end=" ")
        ch = chr(ord(ch)+1)
    print()

print()

# ques4
ch = 'P'
for i in range(1, 5):
    for j in range(1, 5):
        print(ch, end=" ")
        ch = chr(ord(ch)-1)
    print()

print() 

# ques5
for i in range(4, 0, -1):
    ch ='D'
    for j in range(4, 0, -1):
        print(ch, end=" ")
        ch = chr(ord(ch)-1)
    print()

print()

# ques6
ch = 'D'
for i in range(4, 0, -1):
    for j in range(4, 0, -1):
        print(ch, end=" ")
    print()
    ch = chr(ord(ch)-1)