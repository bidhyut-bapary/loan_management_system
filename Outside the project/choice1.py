while True:
    print("1. Add Member")
    print("2. view Member")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print ("Add member selected")
    elif choice == "2":
        print("View member selected")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid Choice")
