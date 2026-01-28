# Recursion : its a process in which the function calls itself until the conditions not made
# def func()
#   base conditional /case
#   recursion calls
# func()

def greet(n):
  # base case
  if n == 0:
    return
  print('hello')
  # recursion call
  greet(n-1)
greet(5)

print()

# increment method
def greet(n):
  # base case
  if n == 6:
    return
  print('hello')
  # recursion call
  greet(n+1)
greet(1)