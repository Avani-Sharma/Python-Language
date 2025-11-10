# Write a Python program that takes a number from the user and checks the following: If divisible by both 3 and 5 - print 'FizzBuzz'; If divisible only by 3 - print 'Fizz'; If divisible only by 5 - print 'Buzz'; Otherwise, print the number itself.

numb = int(input("Enter a number: "))
if numb % 3 == 0 and numb % 5 == 0:
    print("FizzBuzz")
elif numb % 3 == 0:
    print("Fizz")
elif numb % 5 == 0:
    print("Buzz")
else:
    print(numb)



# Accept a number and check if it is a multiple of both 3 and 7.
number = int(input("enter number: "))
if (number%3==0) and (number%7==0):
    print("its multiple of 3 and 7 ")
else:
    print("not a multiple of 3 and 7")



# Accept a number and check if it is divisible by both 3 and 5, otherwise print which one it is divisible by.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3 only")
elif num % 5 == 0:
    print("Divisible by 5 only")
else:
    print("Not divisible by 3 or 5")
