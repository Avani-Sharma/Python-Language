# string formatting using (f-string):
age = 28
name = "Hemant"
a = f"My name is {name} and my age is {age}"
print(a)

# string formatting using (format):
age1 = 21
name1 = "Avani"
x = "My name is {} and my age is {}".format(name1, age1)
print(x)

# modifiers: it is included adding a colon(:) followed by a legal formatting type {.2f means 2 decimals}
price = 59
a = f"The price is {price:.5f} dollars."
print(a)

# placeholders: can contain python code like math operations
a = f"The price is {20*53} dollars."
print(a)