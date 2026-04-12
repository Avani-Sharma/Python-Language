# Create a menu-driven program that displays three food items: 1. Pizza - Rs 200, 2. Burger - Rs 150, 3. Sandwich - Rs 100. Ask the user to select an option by entering the item number. Display the total cost and a thank-you message. Handle invalid choices properly.


print("=== Welcome to Food Corner ===")
print("1. Pizza - Rs 200")
print("2. Burger - Rs 150")
print("3. Sandwich - Rs 100")
choice = int(input("Enter your choice (1-3): "))
if choice == 1:
    no_pizza = int(input("enter no. of pizza"))
    print("You selected Pizza.")
    print("Total cost: ", 200*no_pizza)
elif choice == 2:
    no_burger = int(input("enter no. of burger"))
    print("You selected Burger.")
    print("Total cost: ", 150*no_burger)
elif choice == 3:
    no_sandwitch = int(input("enter no. of sandwich"))
    print("You selected Sandwich.")
    print("Total cost: ", 100*no_sandwitch)
else:
    print("Invalid choice! Please select 1, 2, or 3.")
print("Thank you for your order!")
