# string slicing: is a way to extract a position of string by specifying the start and end index.

# 1. Print all even index characters from "education".
a = "education"
print("A:", a[::2])

# 2. Print all odd index characters from "education".
b ="education"
print("B:", b[1::2])

# 3. From "python", print the first 3 characters using slicing.
c = "python"
print("C:", c[0:3])

# 4. From "python", print the last 3 characters.
d = "python"
print("D:", d[-3:])

# 5. From "programming", print characters from index 2 to 5.
e = "programming"
print("E: ", e[2:5])

# 6. From "hello world", print "world" using slicing.
f = "hello world"
print("F:", f[6:])

# 7. From "python", print the string in reverse using slicing.
g = "python"
print("G:", g[::-1])