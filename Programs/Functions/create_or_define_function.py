def  greeting():
  print("hello")
greeting()

# with parameters
def  greeting(name):
  print(f"hello, {name}")
greeting('avani')

# with user input
def  greeting(name):
  print(f"hello, {name}")
name = input("enter your name")
greeting(name)