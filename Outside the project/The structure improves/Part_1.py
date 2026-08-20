members = [] # List of Dictionaries

def add_member(member_id, name, phone, address, joining_date, status="active"):
    member = {
        "member_id": member_id,
        "name": name,
        "phone": phone,
        "address": address,
        "joining_date": joining_date,
        "status": status
    }
    members.append(member) # Appending the member to the List
    print(f"\n✅ Member added successfully: {name}\n")

# view_member function
def view_members(): # Function to view all the members
    if not members:  # Checring if the member is empty
        print("\n⚠️ No mMembers Found!\n")
        return

    print("\n--- Member List ---\n")
    for member in members:  # Iterating the members list to display the members
        print(f"ID:{member['member_id']} | Name:{member['name']} | Phone:{member['phone']} | Address:{member['address']} | Joining_date:{member['joining_date']} | Status:{member['status']}")
        
        print("\n ------------------")

#Add_Loan Function---------
loans = []  # List of Dictionaries
def add_loan(loan_id, member_id, loan_amount, loan_date, status='active'):
    loan = {
        "loan_id":loan_id,
        "member_id":member_id,
        "loan_amount":loan_amount,
        "loan_date":loan_date,
        "status":status
    }
    loans.append(loan)
    print(f"\n Loan added successfully!:{loan_id}\n")

# view_Loans function
def view_loans():
    if not loans:
        print("\n No Loans found!\n")
        return
    
    print("\n ---Loan List ---\n")
    for loan in loans:
        print(f"Loan ID:{loan['loan_id']} | Member ID: {loan['member_id']} | Loan Amount: {loan['loan_amount']} | Loan Date: {loan['loan_date']} | Status: {loan['status']}")
        print("\n ------------------")

# Add payment function
payments = []
def add_payment(payment_id, loan_id, payment_amount, payment_date):
    payment = {
        "payment_id":payment_id,
        "loan_id":loan_id,
        "payment_amount":payment_amount,
        "payment_date":payment_date
    }
    payments.append(payment)
    print(f"\n Payment added successfully!: {payment_id}\n")

# view payment function
def view_payments():
    if not payments:
        print("\n No Payments Found!\n")
        return

    print("\n --- Payment List ---")
    for payment in payments:
        print(f"Payment ID:{payment['payment_id']} | Loan ID:{payment['loan_id']} | Loan Amount: {payment['payment_amount']} | Payment Date: {payment['payment_date']}")
        print("\n ------------------")
# get total payment function
def get_total_payment(loan_id):
    total = 0
    for payment in payments:
        if payment["loan_id"] == loan_id:
            total = total + payment["payment_amount"]
    return total

# add_member function call
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

# Add Loan Function
def handle_add_loan():
    loan_id = input("Enter Loan ID:")
    if not loan_id:
        print("Loan ID is required!")
    else:
        member_id =input("Enter Member ID:")
        if not member_id:
            print("Member ID is required!")
        else:
            found = False
            for m in members:
                if m['member_id'] == member_id:
                    found = True
                    break
            if not found:
                print("Error: ID does not exist!")
            else:
                loan_amount = input("Enter Loan Amount:")
                if not loan_amount:
                    print("Loan Amount is required!")
                else:
                    loan_date = input("Enter Loan Date(dd-mm-yyyy)")
                    if not loan_date:
                        print("Loan Date is required!")
                    else:
                        # add loan function call
                        add_loan(loan_id,member_id,loan_amount,loan_date)

# Update phone function
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

# delete member function
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

# Add Payment handler function
def handle_add_payment():
    payment_id = input("Enter Payment ID: ")
    if not payment_id:
        print("Payment ID is required!")
    else:
        loan_id = input("Enter Loan ID: ")
        if not loan_id:
            print("Loan ID is required!")
        else:
            # Loan ID টা loans list-এ আছে কিনা চেক করো
            found = False
            for l in loans:
                if l['loan_id'] == loan_id:
                    found = True
                    break
            if not found:
                print("Error: Loan ID does not exist!")
            else:
                payment_amount = input("Enter Payment Amount: ")
                if not payment_amount:
                    print("Payment Amount is required!")
                else:
                    payment_date = input("Enter Payment Date(dd-mm-yyyy): ")
                    if not payment_date:
                        print("Payment Date is required!")
                    else:
                        # add payment function call
                        add_payment(payment_id, loan_id, payment_amount, payment_date)


# Main Menu Loop
while True:
    print("\n ---Main Menu ---")
    print("1. Add Members")
    print("2. View Members")
    print("3. Update Phone Number")
    print("4. Delete Member")
    print("5. Add Loans")
    print("6. View Loans")
    print("7. Add Payment")
    print("8. View Payments")
    print("9. Check Total Payment (Test)")
    print("10. Exit")

# choice handle functions
    choice = input("Enter your choice(1-10): ")

# choice handle functions
    if choice == "1":
        handle_add_member()

    elif choice == "2":
        view_members()

    elif choice == "3":
        handle_update_phone()       
    elif choice == "4":
        handle_delete_member()

    elif choice == "5":
        handle_add_loan()
    elif choice == "6":
        view_loans()
    elif choice == "7":
        handle_add_payment()
    elif choice == "8":
        view_payments()
    elif choice == "9":
        loan_id = input("Enter Loan ID to check total payment: ")
        total = get_total_payment(loan_id)
        print(f"Total Payment for Loan {loan_id}: {total}")
    elif choice == "10":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")