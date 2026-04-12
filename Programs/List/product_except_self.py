# product except self
li = [1,2,3,4]
prod = 1
for ele in li:
    prod *= ele
newlist = []
for i in range(len(li)):
    prod_self = prod // li[i]
    newlist.append(prod_self)
print(newlist)