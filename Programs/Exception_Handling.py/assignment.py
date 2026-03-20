# Write a function that takes two numbers and performs division. Use else block to print
# the result if no error occurs and finally block to print Execution completed.
try:
    a = 10
    b = 10
    c = a/b
except ZeroDivisionError as e:
    print("something has occured into the program", e)
else:
    print(c)
finally:
    print("Execution completed")

print()

# Create a function that converts a given input into integer. Use else block to print the
# converted value and finally block to print Conversion attempt finished.
def fun(a):
    try:
        num = int(a)  
    except ValueError as e:
        print("Conversion failed:", e)
    else:
        print("Converted value:", num)
    finally:
        print("Conversion attempt finished")
fun(20)

print()

# Implement a function that calculates square of a number after converting input to float.
# Use else block to return the square and finally block to display Process done.
def squ(n):
    try:
        num = float(n)
    except:
        print("calculation failed")
    else:
        print(num)
    finally:
        print("process done")
squ(5)

print()

# Write a function that performs floor division of two numbers. Use else block to print
# quotient and finally block to print Function executed.
def fun(a,b):
    try:
        c = a//b
    except ZeroDivisionError as e:
        print("can't divide by zero", e)
    else:
        print(c)
    finally:
        print("function executed")
fun(10,0)

print()

# Create a function that finds reciprocal of a number. Use else block to print the
# reciprocal and finally block to print End of operation.
def fun(a):
    try:
        c = 1/a
    except:
        print("can't find reciprocol if zero")
    else:
        print(c)
    finally:
        print("end of operation")
fun(10)

# Implement a function that multiplies two inputs after converting them into integers. Use
# else block to print product and finally block to print Multiplication tried.
