# ques1
'''
      1
   2     2
 3         3
4 4 4 4 4 4 4
'''
for i in range(1, 5):
    for j in range(4, 0, -1):
            if i == 4 or j == i :
                print(i, end=" ")
            else:
                print(" ", end=" ")
    for j in range(2, i + 1):
        if i == 4 or j == i:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# ques2
'''
4 4 4 4 4 4 4
  3       3
    2   2
      1
'''
for i in range(4,0, -1):
    for j in range(4, 0, -1):
        if i==4 or i==j:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    for j in range(2,i+1):
        if i==4 or j==i:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()