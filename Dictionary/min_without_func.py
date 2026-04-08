min = float('+inf')
d = {
    'a' : 10,
    'b' : 20,
    'c' : 30,
    'd' : 40
}
for key in d:
  if d[key]<min:
    min = d[key]
print(min)

# print its key
min_val = float('+inf')
min_key = ''
d = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}
for key in d:
    if d[key] < min_val:
        min_val = d[key]
        min_key = key
print("Min value:", min_val)
print("Key:", min_key)