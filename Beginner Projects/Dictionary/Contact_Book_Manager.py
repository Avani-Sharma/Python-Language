# project title
print("================= Contact Book Manager =================")

# create an empty dict
contacts = {}

# loop
while True:
    print("\n CONTACT BOOK MENU ")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    # enter user's choice
    choice = int(input("Enter your choice: "))

    # add contact
    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    # display contact
    elif choice == 2:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(name, ":", phone)

    # search contact
    elif choice == 3:
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found")

    # delete contact
    elif choice == 4:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    # update contact
    elif choice == 5:
        name = input("Enter name to update: ")
        if name in contacts:
            new_phone = input("Enter new phone number: ")
            contacts[name] = new_phone
            print("Contact updated")
        else:
            print("Contact not found")
 
    # exit program
    elif choice == 6:
        print("Exiting Contact Book...")
        break
    # invalid choice
    else:
        print("Invalid choice")