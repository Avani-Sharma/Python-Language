# customer name input
name = input("Enter customer name: ")

# printing menu: (coffee-50), (tea-30), (sandwich-70), (burger-100), (pizza-150), (0-exit)
print("1. Coffee   - 50")
print("2. Tea      - 30")
print("3. Sandwich - 70")
print("4. Burger   - 100")
print("5. Pizza    - 150")
print("0. Exit")
print()
# Item quantities
coffee_quantity = tea_quantity = sandwich_quantity = burger_quantity = pizza_quantity = 0
# total bill variable
Total = 0

# take item input from the user
while True:
    item = int(input("Enter item number (0 to finish): "))

    if item == 0:
        break

    quantity = int(input("Enter Quantity: "))

    if item == 1:
        coffee_quantity += quantity
        Total += quantity * 50
    elif item == 2:
        tea_quantity += quantity
        Total += quantity * 30
    elif item == 3:
        sandwich_quantity += quantity
        Total += quantity * 70
    elif item == 4:
        burger_quantity += quantity
        Total += quantity * 100
    elif item == 5:
        pizza_quantity += quantity
        Total += quantity * 150
    else:
        print("Invalid choice!")
print()

# bill print
print("BILL")
print("Customer:", name)
print()
print("Item     Quantity   Price")
if coffee_quantity > 0:
    print("Coffee   ", coffee_quantity, "       ", coffee_quantity * 50)
if tea_quantity > 0:
    print("Tea      ", tea_quantity, "       ", tea_quantity * 30)
if sandwich_quantity > 0:
    print("Sandwich ", sandwich_quantity, "       ", sandwich_quantity * 70)
if burger_quantity > 0:
    print("Burger   ", burger_quantity, "       ", burger_quantity * 100)
if pizza_quantity > 0:
    print("Pizza    ", pizza_quantity,"       ", pizza_quantity * 150)
print()

# total print
print("Subtotal:      ", Total)