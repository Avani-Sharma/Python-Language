# print the welcome message
print("="*60)
print(" "*20, "WELCOME TO CAFE", " "*20)
print("="*60)

# customer name input
name = input("Enter customer name: ")

# printing menu: (coffee-50), (tea-30), (sandwich-70), (burger-100), (pizza-150), (0-exit)
print("1. Coffee          - 50")
print("2. Tea             - 30")
print("3. Sandwich        - 70")
print("4. Burger          - 100")
print("5. Pizza           - 150")
print("0. Exit")

# Item quantities
coffee_q = tea_q = sandwich_q = burger_q = pizza_q = 0

# total bill variable
Total = 0

# take item input from the user
while True:
    item = int(input("\nEnter item number (0 to finish): "))

    if item == 0:
        break

    quantity = int(input("Enter quantity: "))

    if item == 1:
        coffee_q += quantity
        Total += quantity * 50
    elif item == 2:
        tea_q += quantity
        Total += quantity * 30
    elif item == 3:
        sandwich_q += quantity
        Total += quantity * 70
    elif item == 4:
        burger_q += quantity
        Total += quantity * 100
    elif item == 5:
        pizza_q += quantity
        Total += quantity * 150
    else:
        print("Invalid choice!")

# GST calculation
gst = Total * 0.18
grand_total = Total + gst

# discount
discount = 0
if grand_total > 1000:
    discount = grand_total * 0.20
elif grand_total > 500:
    discount = grand_total * 0.10

# final amount
final_amount = grand_total - discount
print("="*60)

# bill print
print(" "*25 ,"BILL" ," "*20)
print("Customer:", name)
print("-"*60)
print("Item                   Quantity                 Price")
print("-"*60)

if coffee_q > 0:
    print("Coffee                 ", coffee_q, "                       ", coffee_q * 50)
if tea_q > 0:
    print("Tea                     ", tea_q, "                           ", tea_q * 30)
if sandwich_q > 0:
    print("Sandwich                ", sandwich_q, "                     ", sandwich_q * 70)
if burger_q > 0:
    print("Burger                   ", burger_q, "                       ", burger_q * 100)
if pizza_q > 0:
    print("Pizza                    ", pizza_q, "                        ", pizza_q * 150)
print()

# total print
print("-"*60)
print("Subtotal:                                        ", Total)
print("GST (18%):                                       ", round(gst, 2))
print("Discount:                                        ", round(discount, 2))
print("-"*60)
print("FINAL AMOUNT:                                    ", round(final_amount, 2))
print()

print("="*60)
print(" "*15,  "THANK YOU! VISIT AGAIN" ," "*10)
print("="*60)