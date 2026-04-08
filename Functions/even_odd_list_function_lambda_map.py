# write a program to add the even or odd string to particular list
# li = [1,2,3,4]
# new_li = ['odd', 'even', 'odd', 'even']

# using function
li = [1, 2, 3, 4]
new_li = []
def fun(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'
for i in li:
    new_li.append(fun(i))
print(new_li)

# using lambda function
li = [1, 2, 3, 4]
new_li = []
check = lambda n: 'even' if n % 2 == 0 else 'odd'
for i in li:
    new_li.append(check(i))
print(new_li)

# using map
li = [1, 2, 3, 4]
new_li = list(map(lambda n: 'even' if n % 2 == 0 else 'odd', li))
print(new_li)