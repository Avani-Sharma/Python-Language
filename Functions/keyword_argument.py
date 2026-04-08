# keyword arguments : at the time of function calling we pass values with the parameter name
# example location ='value', name= 'value'
def show_details (name, location):
  return f"hello, I am {name}. I belongs from {location}"

name = input("enter your name")
location = input("enter your location")
print(show_details(location = location, name = name))