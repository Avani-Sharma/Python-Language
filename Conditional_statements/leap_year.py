# Ask the user to enter a year and check whether it is a leap year or not. Use nested if-else statements to verify the leap year conditions accurately (divisible by 4 but not by 100, except if divisible by 400).

year = int(input("Enter year: "))
if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year")          # Divisible by 4 but not by 100
    else:
        if year % 400 == 0:
            print("Leap year")      # Divisible by 400 → leap year
        else:
            print("Not a leap year")
else:
    print("Not a leap year")



# Check whether the given year is a leap year or not.
Year = int(input("enter the Year: "))
if Year%4==0:
    print("leap year")
elif Year%100==0:
    print("not a leap year")
elif Year%400==0:
    print("leap year")
else:
    print("not a leap year")