# function: it is a block of code which only runs when it is called. 
# function helps avoiding code repetition.

# to create/ defining a function: use the def keyword followed by function name and parentheses

# def  greeting():
#   print("hello")


# calling a function: to call function write its name followed by parentheses
def greeting():
  print("avani")
greeting()

print() 

# you can call the same functions many times
def greeting():
  print("hey, avani")
greeting()
greeting()
greeting()

print()

# with parameters
def  greeting(name):
  print(f"hello, {name}")
greeting('avani')

print()

# with user input
def  greeting(name):
  print(f"hello, {name}")
name = input("enter your name")
greeting(name)

print()

# function names: functions names are case sensitive (myFunction and myfunction both are different)
# function names start with letter or underscore.
# function name can only contain letter, numbers, underscores
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))