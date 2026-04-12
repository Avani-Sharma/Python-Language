# find the common keys between two dictionary
d1 = {'a':10,'b':20,'c':30}
d2 = {'b':5,'c':15,'d':40}
for k in d1:
    if k in d2:
        print(k)

# another method
d1 = {'a':10,'b':20,'c':30}
d2 = {'b':5,'c':15,'d':40}
common = []
for k in d1:
    if k in d2:
        common.append(k)
print(common)