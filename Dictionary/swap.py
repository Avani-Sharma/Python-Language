# swap keys and value pairs
d = {
    'a' : 10,
    'b' : 20,
    'c' : 30
}
e = {}
for key, value in d.items():
  e[value] = key
print(e)

# using membership operator
d = {
    'a': 10,
    'b': 20,
    'c': 30
}
e = {}
for key, value in d.items():
    if value not in e:      
        e[value] = key
print(e)