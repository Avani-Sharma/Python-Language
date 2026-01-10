min = 9
a = {
    'rollno':[1,2,3,4]
}
for i in a['rollno']:
  if i <min:
    min = i
print(min)

# logic using first element
a = {
    'rollno': [1, 2, 3, 4]
}
minimum = a['rollno'][0]
for i in a['rollno']:
  if i <minimum:
    minimum = i
print(minimum)