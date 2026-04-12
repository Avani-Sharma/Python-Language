# Print the length of a string.
s = "avani"
print("length:", len(s))

# Count how many vowels are in a string.
s = "avani"
count = 0
for ch in s:
    if ch in "aeiou":
        count +=1
print("vowels count:", count)

# Count how many consonants are in a string.
s = "avani"
count = 0
for ch in s:
    if ch not in "aeiou":
        count+=1
print("consonant count:", count)

# Check whether a given character exists in a string.
s = "avani"
found = False
for ch in s:
    if ch == 'a':
        found = True
        break
print("found:",found)

# Convert a string to uppercase and lowercase.
s = "avaNI"
print("upper:", s.upper())
print("lower:", s.lower())

# Reverse a string using slicing.
s = "avani"
print("reverse: ", s[::-1])

# reverse a string without using slicing
s = "avani"
for i in range(len(s)-1, -1, -1):
    print("reverse:", s[i], end=" ")

# Print characters at even index positions.
s = "avani"
print("even index:", s[::2])

# Print characters at odd index positions.
s = "avani"
print("odd index:", s[1::2])

# Count spaces in a sentence.
s = "avani sharma jangid"
count = 0
for ch in s:
    if ch == " ":
        count+=1
print("space:", count)

# Remove all spaces from a string.
s = "avani sharma"
remove_space = s.replace(" ", "")
print("remove space:", remove_space)

# Remove all spaces from a string without using replace function
s = "avani sharma"
result = ""
for ch in s:
    if ch != " ":
        result +=ch
print("without space:", result)