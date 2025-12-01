print("========Pattern Menu========")
print("1. Diamond")
print("2. Floyd Triangle")
print("3. Star Pyramid")
print("4. Square Number Pattern")
print("5. Alphabet Triangle")
print()

choice = int(input("Enter your choice (1-5): "))
n = int(input("Enter number of rows: "))

# print diamond 
if choice == 1:
    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for j in range(2, i + 1):
            print("*", end=" ")
        print()

    for i in range(n - 1, 0, -1):
        for j in range(n, 0, -1):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for j in range(2, i + 1):
            print("*", end=" ")
        print()

# print floyd triangle 
elif choice == 2:
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

# print pyramid
elif choice == 3:
    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for j in range(2, i + 1):
            print("*", end=" ")
        print()

# print square pattern
elif choice == 4:
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

# print alphabet pattern 
elif choice == 5:
    ch = 65
    for i in range(n):
        for j in range(i + 1):
            print(chr(ch), end=" ")
        ch += 1
        print()

else:
    print("Invalid choice!")