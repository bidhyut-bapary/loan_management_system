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
        print("\n⚠️ No mMembers Found!\n")
        return
    print("\n--- Member List ---\n")
    for member in members:
        print(f"ID:{member['member_id']} | Name:{member['name']} | Phone:{member['phone']} | Address:{member['address']} | Joining_date:{member['joining_date']} | Status:{member['status']}")

        print("\n -------------")

# Main Menu Loop
while True:
    print("\n ---Main Menu ---")
    print("1. Add Members")
    print("2. View Members")
    print("3. Exit")

    choice = input ("Enter your choice(1-3): ")

    if choice == "1":
        member_id = input("Enter member_id:")
        name = input("Enter your name:")
        phone =input("Enter your phone:")
        address =input("Enter you address:")
        joining_date =input("Enter Joinig Date(dd-mm-yyyy):")

        #add member ফাংশন কল
        add_member(member_id,name,phone,address,joining_date)

    elif choice =="2":
       view_members()
    
    elif choice =="3":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")




        
