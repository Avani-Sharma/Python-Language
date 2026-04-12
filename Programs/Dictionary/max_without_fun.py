max = float('-inf')
d = {
    'a' : 10,
    'b' : 20,
    'c' : 30,
    'd' : 40
}
for key in d:
  if d[key]>max:
    max = d[key]
print(max)

# logic using first element
a = {
    'rollno': [1, 2, 3, 4]
}
maximum = a['rollno'][0]
for i in a['rollno']:
  if i > maximum:
    maximum = i
print(maximum)

# print largest key
max_val = float('-inf')
max_key = ''
d = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}
for key in d:
    if d[key] > max_val:
        max_val = d[key]
        max_key = key
print("Max value:", max_val)
print("Key:", max_key)