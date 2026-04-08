# reverse complete string
s = "avani"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# reverse each word of string
s = "this is sentence"
words = s.split()
result = ""
for w in words:
    result += w[::-1] + " "
print(result)

# reverse word order
s = "avani sharma python"
words = s.split()
rev = words[::-1]
result = " ".join(rev)
print(result)