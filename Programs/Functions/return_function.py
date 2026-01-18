# return values:
# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back.

def  greeting(name):
  return f"hello, {name}"
name = input("enter your name")
message = greeting(name)
print(f"hi, {message}")
print(f"dashboard, {message}")

print()

# You can use the returned value directly:
def get_greeting():
  return "Hello from a function"
print(get_greeting())