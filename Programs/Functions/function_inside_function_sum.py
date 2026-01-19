# write a program to define the function inside function in which you pass 2 no. and inner function prints the sum
# of two numbers and call into the outer functions 
def outer(num1, num2):
  def add(a,b):
    return a+b
  sum = add(num1, num2)
  return sum
result = outer(5, 9)
print(result)