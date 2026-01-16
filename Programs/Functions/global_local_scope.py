# global variable: which is accessible inside or outside of the function
# you can use this variable anywhere into the program
# if you want to value of the global var then use the 'global' keyword to access that variable
var = 1
def count():
  # local variable is accessible only inside the function we can't use this outside the function
  var1 = 2

  # here we're accessing the global varable to change the value of that variable inside the function
  global var
  var = 20

count()
print(var)