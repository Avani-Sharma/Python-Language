# create a dict from two list
li1 = [1,2,3,4,5]
li2 = [10, 20, 30, 40, 50]
d = {}
for i in range(len(li1)):
  if li1[i] not in d:
    d[li1[i]] = li2[i]
print(d)