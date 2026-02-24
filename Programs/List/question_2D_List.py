# 1 Print all elements row-wise.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in li:
    for val in row:
        print(val, end=" ")
print()

# 2 Print all elements column-wise.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(li)
cols = len(li[0])
for j in range(cols):
    for i in range(rows):
        print(li[i][j], end=" ")
print()

# 3 Find the sum of all elements in a 2D list.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
for row in li:
    for val in row:
        sum += val
print("Total sum:", sum)
print()

# 4 Find the maximum element in a 2D list.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max = li[0][0]
for row in li:
    for val in row:
        if val > max:
            max = val
print("Max:", max)
print()

# 5 Find the minimum element in a 2D list.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
min = li[0][0]
for row in li:
    for val in row:
        if val < min:
            min = val
print("Min:", min)
print()

# 6 Count total number of elements in a 2D list.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
count = 0
for row in li:
    count += len(row)
print("Total elements:", count)
print()

# 7 Print each row of a 2D list separately.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in li:
    print("Row:", row)
print()

# 8 Print each column of a 2D list separately.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for j in range(cols):
    col = []
    for i in range(rows):
        col.append(li[i][j])
    print("Column:", col)
print()

# 9 Find the sum of each column.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += li[i][j]
    print("Column sum:", col_sum)
print()

# 10 Print the main diagonal elements..
li = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
for i in range(len(li)):
  for j in range(len(li[i])):
    if i == j:
      print(li[i][j])

# print the secondary diagonal
li = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
for i in range(len(li)):
  for j in range(len(li[i])):
    if i+j ==2:
      print(li[i][j])

# 12 Find the sum of diagonal elements.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diag_sum = 0
for i in range(len(li)):
    diag_sum += li[i][i]
print("Main diagonal sum:", diag_sum)
print()

# 13 Count even numbers in a 2D list.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_count = 0
for row in li:
    for val in row:
        if val % 2 == 0:
            even_count += 1
print("Even count:", even_count)
print()

# 14 Count odd numbers in a 2D list.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odd_count = 0
for row in li:
    for val in row:
        if val % 2 != 0:
            odd_count += 1
print("Odd count:", odd_count)
print()

# 15 Replace all negative numbers with 0.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
li1 = [[3, -1, 5],[-7, 8, -2]]
for i in range(len(li1)):
    for j in range(len(li1[i])):
        if li1[i][j] < 0:
            li1[i][j] = 0
print("After replace:", li1)
print()

# 16 Find the position (row, column) of a given element.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5
f = False
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j] == target:
            print("Position:", (i, j))
            f = True
if not f:
    print("Element not found")
print()

# 17 Check whether a number exists in the 2D list.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 10
exists = False
for row in li:
    if target in row:
        exists = True
        break
print("Exists" if exists else "Not exists")
print()

# 18 Flatten a 2D list into a single list.
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = []
for row in li:
    for val in row:
        flat.append(val)
print("Flatten list:", flat)