members = []

def add_member(member_id, name,phone, address, joining_date, status="active"):
    member = {
        "member_id":member_id,
        "name":name,
        "phone":phone,
        "address":address,
        "joining_date":joining_date,
        "status":status
    }
    members.append(member)
    print("\n Member Added Successfully!\n")

def member_view():
    if not members:
        print("\n No members found!")
        return

    print("\n------ Member List ------")
    for member in members:
        print(f"ID: {member['member_id']} | Name:{member['name']} | Phone:{member['phone']} | Address:{member['address']} | Joining_Date:{member['joining_date']} | Status:{member['status']}")

        print("\n--------------------\n")

# Main Menu

while True:
    print("\n ---Main Menu ---")
    print("1. Add Member")
    print("2. View Member")
    print("3. Update Phone Number")
    print("4. Exit")

    choice = input("Enter your choice(1-4):")
    if choice == "1":
        member_id = input("Enter Member ID:")
        if not member_id:
            print("Member ID is required!")
        else:
            found = False
            for i in members:
                if i["member_id"] == member_id:
                    found = True
                    break
            
            if found:
                print("ID already Exists! Please use a different ID!")
            else:
                name = input("Enter your name:")
                if not name:
                    print("Name is required!")
                else:
                    phone = input("Enter your phone number:")
                    if not phone:
                        print("Phone is required!")
                    else:
                        address = input("Enter your address:")
                        if not address:
                            print("Address is required!")
                        else:
                            joining_date = input("Enter Joining Date(dd-mm-yyyy):")
                            if not joining_date:
                                print("Joining Date is required!")
                            else:
                                # add member function call
                                add_member(member_id, name, phone, address, joining_date)

    elif choice == "2":
        member_view()

    elif choice == "3":
        search_id = input("Enter Member ID to update:")
        if not search_id:
            print("Member ID is required!")
        else:
            target_member = None
            for s in members:
                if s['member_id'] == search_id:
                    target_member = s
                    break
            
            if not target_member:
                print("ID not found!")
            else:
                new_phone = input("Enter New Phone Number:")
                if not new_phone:
                    print("Phone number is required!")
                else:
                    target_member['phone'] = new_phone
                    print("Updated Successfully!")

    elif choice =="4":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice! Please Choose Between 1-4!")





