# replace(): replace string with another string
a = "avani sharma"
print(a.replace("sharma", "jangid"))

# strip(): remove whitespace
a = "               avani          sharma    "
print(a.strip())

# lstrip(): remove left whitespace
a = "     avani sharma"
print(a.lstrip())

# rstrip(): remove right whitespace
a = "avani sharma         "
print(a.rstrip())

# split(): splits the string from the left (beginning).
a = "avani sharma"
print(a.split())

# rsplit(): splits the string from the right (end).
a = "avani sharma"
print(a.rsplit(","))

# join(): join the elements of an iterable to the end of string.
a = "avani sharma"
w="#".join(a)
print(w)