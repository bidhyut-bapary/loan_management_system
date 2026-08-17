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
    print(f"\n✅ Member added successfully! ID: {member_id}, Name: {name}\n")


def view_members():
    if not members:
        print("\n⚠️ No members found!\n")
        return
    
    print("\n--- Member List ---")
    for member in members:
        print(f"ID: {member['member_id']} | Name: {member['name']} | Phone: {member['phone']} | Status: {member['status']}")
    print("-------------------\n")


# Main Menu Loop
while True:
    print("1. Add Member")
    print("2. View Members")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        found = False
        member_id = input("Enter Member ID: ")
        for i in members:
            if i['member_id'] == member_id:
                found = True
                break
        if found:
            print("\n⚠️ এই ID ইতিমধ্যে আছে! অনুগ্রহ করে অন্য ID দিন।\n")
        else:
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")
            joining_date = input("Enter Joining Date (DD-MM-YYYY): ")
            add_member(member_id, name, phone, address, joining_date)

    elif choice == "2":
        view_members()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice. Please try again.\n")
