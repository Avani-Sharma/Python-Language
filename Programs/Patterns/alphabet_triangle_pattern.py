# Triangle of alphabets
'''
A
A B
A B C
A B C D
A B C D E
'''
for i in range(6):
    for j in range(65, 65+i):
        print(chr(j), end=" ")
    print()