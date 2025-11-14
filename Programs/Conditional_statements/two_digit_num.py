# Accept a number and check if it is a two-digit number.


num = int(input("Enter a number: "))
if num >= 10 and num <= 99:
    print("Two-digit number")
else:
    print("Not a two-digit number")
