# 1. Accept three numbers a, b, and c from the user and compute the value of (a + b) ** 2 - (a - b) ** 2. Then verify whether it equals 4 * a * b. Print all steps and the comparison result.
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
d = (a+b)**2-(a-b)**2
print(d)
e = 4*a*b
print("Comparison result →", d==e)



# 2. Evaluate (100 / 5 * 2 + 10 - 3 ** 2) in Python. 
result = (100 / 5 * 2 + 10 - 3 ** 2)
print(result)


# 3. Use three Boolean variables x = True, y = False, and z = True. Evaluate and print the results of: x or y and z, and (x or y) and z.
x = True 
y = False
z = True
print(x or y and z)
print((x or y)and z)