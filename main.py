from members import members, add_member, view_members, handle_add_member, handle_update_phone, handle_delete_member
from loans import loans, add_loan, view_loans, handle_add_loan
from payments import payments, add_payment, view_payments, get_total_payment, get_outstanding_balance, handle_add_payment, handle_check_total_payment, handle_check_balance

# Main Menu Loop
while True:
    print("\n--- Main Menu ---")
    print("1.  Add Member")
    print("2.  View Members")
    print("3.  Update Phone Number")
    print("4.  Delete Member")
    print("5.  Add Loan")
    print("6.  View Loans")
    print("7.  Add Payment")
    print("8.  View Payments")
    print("9.  Check Total Payment")
    print("10. Check Balance")
    print("11. Exit")

    choice = input("\nEnter your choice (1-11): ")

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
        handle_check_total_payment()
    elif choice == "10":
        handle_check_balance()
    elif choice == "11":
        print("\nGoodbye! 👋\n")
        break
    else:
        print("\n⚠️ Invalid Choice! Please enter 1-11.\n")
