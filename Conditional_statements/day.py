# Accept a day number (1-7) from the user and display the corresponding day name (e.g., 1 for Monday, 2 for Tuesday, etc.). If an invalid number is entered, print 'Invalid day number.


day = int(input("enter day number(1-7):"))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid day number")
    