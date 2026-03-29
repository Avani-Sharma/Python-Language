print("============================ ATM Machine ============================")
# initial data
pin = 1234
balance = 1000

# PIN check
try:
    entered_pin = int(input("Enter PIN: "))
except ValueError:
    print("PIN should be numbers only")
    exit()

if entered_pin != pin:
    print("Wrong PIN")
    exit()

print("Login Successful")

# loop
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter valid number")
        continue

    # Check Balance
    if choice == 1:
        print(f"Your Balance: {balance}")

    # Deposit
    elif choice == 2:
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")
            balance += amount
            print("Deposit successful")
        except ValueError as e:
            print(e)

    # Withdraw
    elif choice == 3:
        try:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                raise ValueError("Invalid amount")
            if amount > balance:
                raise Exception("Insufficient balance")
            balance -= amount
            print("Withdrawal successful")
        except Exception as e:
            print(e)

    # Exit
    elif choice == 4:
        print("Thank you 😊")
        break

    else:
        print("Invalid option")