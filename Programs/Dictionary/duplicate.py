# print all duplicates of the list 
li = [1,2,3,2,1,3,3,2,5,6,7,8]
d = {}
for i in li:
  if i not in d:
    d[i] = 1
  else:
    d[i] += 1
for key, value in d.items():
  if value>1:
    print(key)