# project title
print("=================== Interactive Text Analyzer ===================")

# take input sentence from user
text = input("Enter a sentence: ")

# loop 
while True:

    # create options
    print("\nChoose an option:")
    print("1. Count total characters")
    print("2. Count vowels & consonants")
    print("3. Reverse the text")
    print("4. Check palindrome")
    print("5. Convert case")
    print("6. Word count")
    print("7. Exit")

    # take user's choice
    choice = input("Enter your choice (1-7): ")

    # 1: count total characters
    if choice == "1":
        print(f" Total Characters: {len(text)}")

    # 2: count vowels and consonants
    elif choice == "2":
        vowels = "aeiouAEIOU"   
        v = 0                 
        c = 0                 

        for ch in text:
            if ch in vowels:
                v += 1
            elif ch.isalpha():  
                c += 1

        print(f" Vowels: {v} | Consonants: {c}")

    # 3: reverse the text
    elif choice == "3":
        print(f" Reversed Text: {text[::-1]}")

    # 4: to check palindrome
    elif choice == "4":
        cleaned = text.replace(" ", "").lower()

        if cleaned == cleaned[::-1]:
            print(" This is a Palindrome!")
        else:
            print(" Not a Palindrome!")

    # 5: convert case
    elif choice == "5":
        print(f" Uppercase: {text.upper()} | Lowercase: {text.lower()} | Title Case: {text.title()}")

    # 6: count words
    elif choice == "6":
        words = text.split()   
        print(f" Total Words: {len(words)}")

    # 7: Exit program
    elif choice == "7":
        print("Thank you for using the Interactive Text Analyzer!")
        break

    # invalid choice
    else:
        print("Invalid choice! Please try again.")