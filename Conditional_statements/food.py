# Create a menu-driven program that displays three food items: 1. Pizza - Rs 200, 2. Burger - Rs 150, 3. Sandwich - Rs 100. Ask the user to select an option by entering the item number. Display the total cost and a thank-you message. Handle invalid choices properly.


print("=== Welcome to Food Corner ===")
print("1. Pizza - Rs 200")
print("2. Burger - Rs 150")
print("3. Sandwich - Rs 100")
choice = int(input("Enter your choice (1-3): "))
if choice == 1:
    print("You selected Pizza.")
    print("Total cost: Rs 200")
elif choice == 2:
    print("You selected Burger.")
    print("Total cost: Rs 150")
elif choice == 3:
    print("You selected Sandwich.")
    print("Total cost: Rs 100")
else:
    print("Invalid choice! Please select 1, 2, or 3.")
print("Thank you for your order!")
