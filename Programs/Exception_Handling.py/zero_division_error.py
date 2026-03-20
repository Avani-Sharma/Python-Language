# zero division error
def divide(a, b):
    # whenever any input into the function then it executes the try block
    try:
        result = a/b
        return result
    # if there is any exception into the try block then this except block will run
    except ZeroDivisionError:
        return "Some thing has occured!"
print(divide(10, 0))