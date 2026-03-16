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
  # base condition: if condition is true then the function call would be stopped.
  if n == 5:
    return
  print('hello')
  # recursion call: this function call is nothing but the recursion call for the next numbers.
  greet(n+1)
greet(1)