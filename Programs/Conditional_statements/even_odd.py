# Accept a number from the user and check if it is even or odd.

num = int(input())
if num%2==0:
    print("even")
else:
    print("odd")


# Accept a number and print “Even Positive”, “Odd Positive”, or “Negative”.

number = int(input("enter number"))
if number>0 and number%2==0:
    print("even positive")
elif number>0 and  number%2!=0:
    print("odd positive")
else:
    print("negative")