# project
print("================ Unique Product Tracker ===============")

# set 
products = {"Laptop", "Phone", "Headphones"}

# loop
while True:
    print("\n Unique Product Tracker ")
    print("1. Display Products")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Search Product")
    print("5. Exit")
    
    # take user's choice
    choice = input("Enter your choice (1-5): ")
    
    # display all products
    if choice == "1":
        print("\nAvailable Products:")
        for p in products:
            print("-", p)
    
    # add a new product
    elif choice == "2":
        new_product = input("Enter product name to add: ").title()  
        if new_product in products:  
            print(f"{new_product} already exists!")
        else:
            products.add(new_product) 
            print(f"{new_product} added successfully.")
    
    # remove a product
    elif choice == "3":
        del_product = input("Enter product name to remove: ").title()
        if del_product in products:  
            products.remove(del_product)
            print(f"{del_product} removed successfully.")
        else:
            print(f"{del_product} not found!")
    
    # search for a product
    elif choice == "4":
        search = input("Enter product name to search: ").title()
        if search in products: 
            print(f"{search} exists in the tracker.")
        else:
            print(f"{search} not found!")
    
    # exit program
    elif choice == "5":
        print("Exiting...")
        break
    
    # invalid input
    else:
        print("Invalid choice! Try again.")