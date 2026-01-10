# project title
print("================= Number Analyzer =================")

# empty list to store numbers
numbers = []

# loop
while True:

    # create options
    print("\n NUMBER ANALYZER MENU")
    print("1. Add Numbers")
    print("2. Display Numbers")
    print("3. Even Numbers")
    print("4. Odd Numbers")
    print("5. Sum of Numbers")
    print("6. Maximum Number")
    print("7. Minimum Number")
    print("8. Exit")

    # take user's choice
    choice = int(input("Enter your choice: "))

    # 1: add numbers to the list
    if choice == 1:
        n = int(input("How many numbers you want to add: "))
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)   
        print("Numbers added successfully!")

    # 2: display all numbers
    elif choice == 2:
        print("Number List:", numbers)

    # 3: display even numbers
    elif choice == 3:
        even = []
        for num in numbers:
            if num % 2 == 0:
                even.append(num)
        print("Even Numbers:", even)

    # 4: display odd numbers
    elif choice == 4:
        odd = []
        for num in numbers:
            if num % 2 != 0:
                odd.append(num)
        print("Odd Numbers:", odd)

    # 5: calculate sum of numbers
    elif choice == 5:
        total = 0
        for num in numbers:
            total += num
        print("Sum of Numbers:", total)

    # 6: find maximum number
    elif choice == 6:
        if len(numbers) == 0:
            print("List is empty")
        else:
            max_num = numbers[0]   
            for num in numbers:
                if num > max_num:
                    max_num = num
            print("Maximum Number:", max_num)

    # 7: find minimum number
    elif choice == 7:
        if len(numbers) == 0:
            print("List is empty")
        else:
            min_num = numbers[0]  
            for num in numbers:
                if num < min_num:
                    min_num = num
            print("Minimum Number:", min_num)

    # 8: exit the program
    elif choice == 8:
        print("Exiting program... Thank you ")
        break   

    # invalid choice 
    else:
        print("Invalid choice! Please try again.")