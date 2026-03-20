# try-except-else-finally:
# finally block will always run either any exception or any error occur during execution of the program.
# this is basically used into the file I/O operations.

try:
    a = '10'
    b = 10
    c = a+b
except TypeError as e:
    print("something has occured into the program", e)
else:
    print("this block will run after the try block")
    print(c)
finally:
    print("this block will always ")

print()

# another example without error 
try:
    a = 10
    b = 10
    c = a+b
except TypeError as e:
    print("something has occured into the program", e)
else:
    print("this block will run after the try block")
    print(c)
finally:
    print("this block will always ")