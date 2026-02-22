# print the index of target sum
li = [1,2,3,4,5]
t = 7
for i in range(len(li)):
  for j in range(i+1, len(li)):
    if li[i] + li[j] == t:
      print(i, j)