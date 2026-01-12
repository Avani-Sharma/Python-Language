# write a program to create a set using list of the elements
li = [1, 2, 3, 5, 5]
s = set(li)
print(s)

# write a program to take 5 inputs from the user and add each element to the set
# brute force approach
s = set()
print("5 elements")
for i in range(5):
    value = int(input("Enter element: "))
    s.add(value)
print(s)

# another method
element = set(map(int, input('enter elements: ').split()))
print(element)