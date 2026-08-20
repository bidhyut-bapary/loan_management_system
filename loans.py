# loan সংক্রান্ত সব function
from members import members

loans = []  # List of Dictionaries

# Add Loan Function
def add_loan(loan_id, member_id, loan_amount, loan_date, status='active'):
    loan = {
        "loan_id": loan_id,
        "member_id": member_id,
        "loan_amount": loan_amount,
        "loan_date": loan_date,
        "status": status
    }
    loans.append(loan)
    print(f"\n✅ Loan added successfully!: {loan_id}\n")

# View Loans Function
def view_loans():
    if not loans:
        print("\n⚠️ No Loans found!\n")
        return

    print("\n--- Loan List ---\n")
    for loan in loans:
        print(f"Loan ID:{loan['loan_id']} | Member ID: {loan['member_id']} | Loan Amount: {loan['loan_amount']} | Loan Date: {loan['loan_date']} | Status: {loan['status']}")
        print("\n ------------------")

# Handle Add Loan
def handle_add_loan():
    loan_id = input("Enter Loan ID: ")
    if not loan_id:
        print("Loan ID is required!")
    else:
        # Check duplicate loan ID
        for l in loans:
            if l['loan_id'] == loan_id:
                print("Error: Loan ID already exists!")
                return
        member_id = input("Enter Member ID: ")
        if not member_id:
            print("Member ID is required!")
        else:
            # Check member exists
            found = False
            for m in members:
                if m['member_id'] == member_id:
                    found = True
                    break
            if not found:
                print("Error: Member ID does not exist!")
            else:
                loan_amount = int(input("Enter Loan Amount: "))
                if not loan_amount:
                    print("Loan Amount is required!")
                else:
                    loan_date = input("Enter Loan Date (dd-mm-yyyy): ")
                    if not loan_date:
                        print("Loan Date is required!")
                    else:
                        add_loan(loan_id, member_id, loan_amount, loan_date)
