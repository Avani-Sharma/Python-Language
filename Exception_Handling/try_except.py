# try-except is used to catch and handle runtime errors in a program

try:
    print(10/0)
except ZeroDivisionError as e:
    print("something has occured!", e)