# error: An error is a serious problem in the program. It usually happens due to wrong syntax or code 
# structure. The program does not run at all. Hard (or not possible) to handle.

# Exceptions: An exception occurs during program execution (runtime). The program starts running but 
# stops when the issue occurs. It can be handled using try-except block.
# First the try block will run. If there is any exception has occuring during the execution of try
# block then the except block will run.
# syntax: 
# try:
#    expression for the executing the code 
# except exception_error:
#     print the message why this exception has occured 

# try-except is used to catch and handle runtime errors in a program

try:
    print(10/0)
except ZeroDivisionError as e:
    print("something has occured!", e)