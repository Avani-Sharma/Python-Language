try:
    balance = 5000
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        raise Exception("Insufficient balance")

    print("Processing transaction...")

except ValueError:
    print("Invalid amount entered!")

except Exception as e:
    print("Error:", e)

else:
    print("Transaction successful! Collect your cash ")

finally:
    print("Thank you for using the ATM ")