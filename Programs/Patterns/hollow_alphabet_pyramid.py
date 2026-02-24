'''
      A
    B   B
  C       C
D D D D D D D
'''
ch = 'A'
for i in range(1, 5):
    for j in range(4, 0, -1):
        if i == 4 or j == i:
            print(ch, end=" ")
        else:
            print(" ", end=" ")
    for j in range(2, i+1):
        if i == 4 or j == i:
            print(ch, end=" ")
        else:
            print(" ", end=" ")
    
    print()
    ch = chr(ord(ch) + 1) 