# write a function student_info (name, age, city) print all the info
def  greeting(name= 'user', age='user age', city = 'user city'):
  return f"hello {name}, age {age}, city  {city}"
name = input("enter your name")
age = int(input("enter age"))
city = input("enter your city")
print(greeting(name, age, city))