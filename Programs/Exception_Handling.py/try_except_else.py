# try-except-else:
# else block will run when the try block successfully executed. It means when there is no exception is occured.
# try → run code
# except → handle error (if occurs)
# else → run code only if no error occurs

# syntax:
# try:
    # risky code
# except:
    # runs if error occurs
# else:
    # runs if no error


try:
    a = '10'
    b = 10
    c = a+b
except TypeError as e:
    print("something has occured into the program", e)
else:
    print(c)