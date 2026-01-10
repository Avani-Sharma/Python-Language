sum = 0
a = {
    'rollno':[1,2,3,4]
}
for i in a['rollno']:
  sum += i
print(sum)

# for loop with index
a = {
  'rollno': [1, 2, 3, 4]
}
total = 0
for i in range(len(a['rollno'])):
  total += a['rollno'][i]
print(total)