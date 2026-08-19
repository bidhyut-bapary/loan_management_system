members = []

def add_member(member_id, name, phone, address, joining_date, status="active"):
    member = {
        "member_id": member_id,
        "name": name,
        "phone": phone,
        "address": address,
        "joining_date": joining_date,
        "status": status
    }
    members.append(member)
    print(f"\n✅ Member added successfully: {name}\n")

def view_members():
    if not members:
        print("\n⚠️ No Members Found!\n")
        return

    print("\n--- Member List ---\n")
    for member in members:
        print(f"ID:{member['member_id']} | Name:{member['name']} | Phone:{member['phone']} | Address:{member['address']} | Joining_date:{member['joining_date']} | Status:{member['status']}")
        print("\n -------------")

loans = []
# Add_Loan function---------
def add_loan(loan_id, member_id, loan_amount, loan_date, status="active"):
    loan = {
        "loan_id":loan_id,
        "member_id":member_id,
        "loan_amount":loan_amount,
        "loan_date":loan_date,
        "status":status
    }
    loans.append(loan)
    print(f"\n Loan added successfully! Loan ID: {loan_id}\n")

def handle_add_member():
    found = False
    member_id = input("Enter member_id:")
    if not member_id:
        print("Member ID is required!")
    else:
        for i in members:
            if i['member_id'] == member_id:
                found = True
                break
        if found:
            print("Error: Id already Exist! Please use different Id!")
        else:
            name = input("Enter your name:")
            if not name:
                print("Name is required!")
            else:
                phone = input("Enter your phone:")
                if not phone:
                    print("Phone is required!")
                else:
                    address = input("Enter your address:")
                    joining_date = input("Enter Joining Date(dd-mm-yyyy):")
                    if not joining_date:
                        print("Joining Date is required!")
                    else:
                        # add member ফাংশন কল
                        add_member(member_id, name, phone, address, joining_date)

def handle_update_phone():
    search_id = input("Enter Member ID to Update Phone:")
    if not search_id:
        print("Member ID is required!")
    else:
        new_phone = input("Enter new phone number:")
        found = False
        for s in members:
            if s['member_id'] == search_id:
                s['phone'] = new_phone
                found = True
                print("Updated Successfully!")
                break
        if not found:
            print("Member ID not found!")

def handle_delete_member():
    search_id = input("Enter Member ID to Delete:")
    if not search_id:
        print("Member ID is required!")
    else:
        found = False
        for s in members:
            if s['member_id'] == search_id:
                members.remove(s)
                found = True
                print("Deleted Successfully!")
                break
        if not found:
            print("Member ID not found!")

# Main Menu Loop
while True:
    print("\n ---Main Menu ---")
    print("1. Add Members")
    print("2. View Members")
    print("3. Update Phone Number")
    print("4. Delete Member")
    print("5. Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        handle_add_member()

    elif choice == "2":
        view_members()
    
    elif choice == "3":
        handle_update_phone()

    elif choice == "4":
        handle_delete_member()

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")
