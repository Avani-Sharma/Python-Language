# default argument: into this argument we basically pass the default value with the parameter
def  greeting(name= 'user'):
  return f"hello, {name}"
name = input("enter your name")
message = greeting(name)
print(f"hi, {message}")
print(f"dashboard, {message}")