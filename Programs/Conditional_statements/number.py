'''Write a Python program that checks if the given number is positive, negative, or zero. If it's positive, check whether it is even or odd and print both conditions clearly.'''



number = int(input("Enter a number: "))
if number > 0:
    print("The number is Positive")
    if number % 2 == 0:
        print("It is Even")
    else:
        print("It is Odd")

elif number < 0:
    print("The number is Negative")
    if number % 2 == 0:
        print("It is Even")
    else:
        print("It is Odd")

else:
    print("The number is Zero")
