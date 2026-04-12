# convert into list of fahrenheit
# formula: (c* 9/5)+32
# li = [0, 20, 30, 40]

# function
li = [0, 20, 30, 40]
new_li = []
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
for i in li:
    new_li.append(celsius_to_fahrenheit(i))
print(new_li)

# using lambda function
li = [0, 20, 30, 40]
new_li = []
convert = lambda c: (c * 9/5) + 32
for i in li:
    new_li.append(convert(i))
print(new_li)

# using map
li = [0, 20, 30, 40]
new_li = list(map(lambda c: (c * 9/5) + 32, li))
print(new_li)