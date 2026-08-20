# payment সংক্রান্ত সব function
from loans import loans

payments = []  # List of Dictionaries

# Add Payment Function
def add_payment(payment_id, loan_id, payment_amount, payment_date):
    payment = {
        "payment_id": payment_id,
        "loan_id": loan_id,
        "payment_amount": payment_amount,
        "payment_date": payment_date
    }
    payments.append(payment)
    print(f"\n✅ Payment added successfully!: {payment_id}\n")

# View Payments Function
def view_payments():
    if not payments:
        print("\n⚠️ No Payments Found!\n")
        return

    print("\n--- Payment List ---")
    for payment in payments:
        print(f"Payment ID:{payment['payment_id']} | Loan ID:{payment['loan_id']} | Payment Amount: {payment['payment_amount']} | Payment Date: {payment['payment_date']}")
        print("\n ------------------")

# Get Total Payment Function
def get_total_payment(loan_id):
    total = 0
    for payment in payments:
        if payment["loan_id"] == loan_id:
            total = total + payment["payment_amount"]
    return total

# Get Outstanding Balance Function
def get_outstanding_balance(loan_id):
    loan_amount = 0
    for loan in loans:
        if loan['loan_id'] == loan_id:
            loan_amount = loan["loan_amount"]
            break
    total_paid = get_total_payment(loan_id)
    outstanding = loan_amount - total_paid
    return outstanding

# Handle Add Payment
def handle_add_payment():
    payment_id = input("Enter Payment ID: ")
    if not payment_id:
        print("Payment ID is required!")
    else:
        loan_id = input("Enter Loan ID: ")
        if not loan_id:
            print("Loan ID is required!")
        else:
            # Loan ID আছে কিনা চেক করো
            found = False
            for loan in loans:
                if loan['loan_id'] == loan_id:
                    found = True
                    break
            if not found:
                print("\n⚠️ Loan ID not found!\n")
            else:
                payment_amount = int(input("Enter Payment Amount: "))
                if not payment_amount:
                    print("Payment Amount is required!")
                else:
                    payment_date = input("Enter Payment Date (dd-mm-yyyy): ")
                    if not payment_date:
                        print("Payment Date is required!")
                    else:
                        add_payment(payment_id, loan_id, payment_amount, payment_date)

# Handle Check Total Payment
def handle_check_total_payment():
    loan_id = input("Enter Loan ID to check total payment: ")
    if not loan_id:
        print("Loan ID is required!")
    else:
        total = get_total_payment(loan_id)
        print(f"\n Total Payment for Loan {loan_id} is: Tk {total}\n")

# Handle Check Balance
def handle_check_balance():
    loan_id = input("Enter Loan ID: ")
    if not loan_id:
        print("Loan ID is required!")
    else:
        found = False
        for loan in loans:
            if loan['loan_id'] == loan_id:
                found = True
                break
        if not found:
            print("\n⚠️ Loan ID Not Found!\n")
        else:
            balance = get_outstanding_balance(loan_id)
            print(f"\n Outstanding balance for Loan {loan_id} is: Tk {balance}\n")