# Recursion : its a process in which the function calls itself until the conditions not made
# def func()
#   base conditional /case
#   recursion calls
# func()

# example 
def greet(n):
  # base condition: if condition is true then the function call would be stopped.
  if n == 5:
    return
  print('hello, from the function')
  # recursion call: this function call is nothing but the recursion call for the next numbers.
  greet(n+1)
greet(1)


# example
def fun(n):
  if n==6:
    return 
  print("number is: ", n)
  fun(n+1)
fun(1)