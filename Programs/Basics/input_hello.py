# take two variables, a and b and also take separator.
a = input()
b = input()
separator = input()[0]

# With space: Print a and b in a single line, separated by a space, followed by a newline.
print(a, b)

# Without newline: Print a and b separated by a space, but do not end the output with a newline.
print(a, b, end ="")

# With separator: Print a and b separated by a specified separator, followed by a newline.
print(a + separator + b)

# Without space: Print a and b in a single line, with no spaces between them, followed by a newline.
print(a+b)