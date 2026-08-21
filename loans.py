# loan সংক্রান্ত সব function
import json
from members import members

loans = []  # List of Dictionaries

# JSON function
def save_loans():
    with open("loans.json", "w") as file:
        json.dump(loans, file, indent=4)

# Load loan function
def load_loans():
    global loans
    try:
        with open("loans.json", "r") as file:
            loans = json.load(file)
    except FileNotFoundError:
        print("\n No file found!\n")
        loans = []

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
    save_loans()
    print(f"\n✅ Loan added successfully!: {loan_id}\n")

# View Loans Function
def view_loans():
    if not loans:
        print("\n⚠️ No Loans found!\n")
        return

    print("\n--- Loan List ---\n")
    for loan in loans:
        print(
            f"Loan ID:{loan['loan_id']} |"
            f" Member ID: {loan['member_id']} | "
            f"Loan Amount: {loan['loan_amount']} |" 
            f"Loan Date: {loan['loan_date']} |"
            f"Status: {loan['status']}"
         )
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
                try:
                    loan_amount = int(input("Enter Loan Amount: "))
                except ValueError:
                    print("\n ⚠️ Invalid amount! Loan Amount must be a number.\n ")
                    return
                loan_date = input("Enter Loan Date (dd-mm-yyyy): ")
                if not loan_date:
                    print("Loan Date is required!")
                else:
                    add_loan(
                        loan_id,
                        member_id,
                        loan_amount,
                        loan_date
                    )



