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
        print(num**2)
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

print()

# Implement a function that multiplies two inputs after converting them into integers. Use
# else block to print product and finally block to print Multiplication tried.
def fun(a, b):
    try:
        c = int(a) * int(b)
    except:
        print("something has occured into the program")
    else:
        print(c)
    finally:
        print("multiplication tried")
fun(10,10)

print()

# Write a function that calculates percentage using marks and total marks. Use else
# block to print percentage and finally block to print Calculation finished.
def fun(marks, total):
    try:
        marks = int(marks)
        total = int(total)
        c = (marks / total) * 100
    except Exception as e:
        print("Something has occurred in the program:", e)
    else:
        print(c)
    finally:
        print("Calculation finished")
fun(35, 50)

print()

# Create a function that converts string input into float and prints half of it. Use else block
# for output and finally block for completion message.
def fun(x):
    try:
        num = float(x)
        c = num / 2
    except:
        print("something has occured into the program")
    else:
        print(c)
    finally:
        print("completion message")
fun(24)

print()

# Implement a function that performs modulus operation. Use else block to print
# remainder and finally block to print Modulus attempt done.
def fun(y,z):
    try:
        c = y%z
    except:
        print("spmething occured")
    else:
        print(c)
    finally:
        print("modulus attempt done")
fun(45, 5)

print()

# Write a function that calculates power of a number. Use else block to print result and
# finally block to print Power function executed.
def fun(m, n):
    try:
        c = int(m**n)
    except Exception as e:
        print("Something occurred:", e)
    else:
        print(c)
    finally:
        print("Power function executed")
fun(10, 2)

print()

# Create a function that returns absolute value after converting input safely. Use else
# block to print absolute value and finally block to print Absolute check completed.
def fun(e):
    try:
        c = abs(e)
    except:
        print("something occured")
    else:
        print(c)
    finally:
        print("Absolute check completed")
fun(-3)

print()

# Implement a function that divides three numbers step by step. Use else block to print
# final result and finally block to print Division process ended.
def divide_three(a, b, c):
    try:
        step1 = a / b
        step2 = step1 / c
    except Exception as e:
        print("Something went wrong:", e)
    else:
        print(step2)
    finally:
        print("Division process ended")
divide_three(20, 2, 5)

print()

# Write a function that converts input into integer and prints its double. Use else block for
# result and finally block for closing message.
def fun(o):
    try:
        num = int(o)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print("Double of number is:", num * 2)
    finally:
        print("Program finished")
fun(12)

print()

# Create a function that subtracts two numbers after safe conversion. Use else block to
# print difference and finally block to print Subtraction attempt finished.
def fun(p,q):
    try:
        c = int(p) - int(q)
    except:
        print("something occured")
    else:
        print(c)
    finally:
        print("Subtraction attempt finished")
fun(45, 7)

print()

# Implement a function that calculates average of two numbers. Use else block to print
# average and finally block to print Average calculation done.
def fun(r,s):
    try:
        c = (int(r) + int(s)) / 2
    except:
        print("something occured")
    else:
        print(c)
    finally:
        print("average calculation done")
fun(8,9)

print()

# Write a function that calculates square root after converting input to float. Use else
# block to print result and finally block to print Square root operation finished.
def fun(k):
    try:
        num = float(k)
        c = num ** 0.5
    except:
        print("something occured")
    else:
        print(c)
    finally:
        print("sqrt operation finished")
fun(2)

print()

# Create a function that performs simple interest calculation. Use else block to print
# interest and finally block to print Interest calculation attempt done.
def funct(P, R, T):
    try:
        SI = (float(P) * float(R) * float(T)) / 100
    except Exception as e:
        print("something occured", e)
    else:
        print(SI)
    finally:
        print("interest calculation attempt done")
funct(1000 , 5, 2)

print()

# Implement a function that divides a number by itself after safe conversion. Use else
# block to print result and finally block to print Self division completed.
def functi(l):
    try:
        num = float(l)
        c = num / num
    except:
        print("something occured")
    else:
        print(c)
    finally:
        print("self division completed")
functi(67)

print()

# Write a function that finds remainder after safe integer conversion of inputs. Use else
# block to print remainder and finally block to print Remainder operation finished.
def functi(a, b):
    try:
        rem = int(a) % int(b)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Remainder is:", rem)
    finally:
        print("Remainder operation finished")
functi(10, 3)

print()

# Create a function that performs multiplication of three numbers. Use else block to print
# product and finally block to print Multiplication process completed.
def mul(a,b,c):
    try:
        d = int(a) * int(b) * int(c)
    except:
        print("something occured")
    else:
        print(d)
    finally:
        print("mulitplication process completed ")
mul(3,2,1)