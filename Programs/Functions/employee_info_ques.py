# write a function to display the details of the employees name, dept, salary call it using the
# positional arguments as well as keywords arguments
def employee (name, dept, salary):
  return f"hello, I am {name}, dept {dept}, salary {salary}"

# positional arguments
employee ('avani', 'HR', 50000)

# keyword arguments
employee (name = 'avani', dept = 'HR', salary = 50000)