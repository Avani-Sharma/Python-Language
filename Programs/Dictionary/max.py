max = 0
a = {
    'rollno':[1,2,3,4]
}
for i in a['rollno']:
  if i > max:
    max = i
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