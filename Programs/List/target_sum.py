# print the index of target sum
li = [3,2,4]
t = 7
for i in range(len(li)):
  for j in range(i+1, len(li)):
    if li[i] + li[j] == t:
      print(i, j)