# positional arguments : are the arguments which are passed on the basis of the function definition 
# based on their parameter position. 
def show_details (name, location):
  return f"hello, I am {name}. I belongs from {location}"
print(show_details('avani', 'bhiwadi'))

# example
def student(name, age):
  print(name, age)
student("avani", 22)