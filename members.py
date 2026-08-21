import json

members = [] # List of Dictionaries

# JSON function
def save_members():
    with open("members.json", "w") as file:
        json.dump(members, file, indent=4)
# Load Json function
def load_members():
    global members
    try:
        with open("members.json", "r") as file:
            members= json.load (file)
    except FileNotFoundError:
        print ("No file found!")
        members = []

# Add member function

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
    save_members()
    print(f"\n✅ Member added successfully: {name}\n")

# view member function
def view_members(): # Function to view all the members
    if not members:  # Checring if the member is empty
        print("\n⚠️ No Members Found!\n")
        return

    print("\n--- Member List ---\n")
    for member in members:  # Iterating the members list to display the members
        print(
            f"ID: {member['member_id']} | "
            f"Name: {member['name']} | "
            f"Phone: {member['phone']} | "
            f"Address: {member['address']} | "
            f"Joining Date: {member['joining_date']} | "
            f"Status: {member['status']}"
        )      
        print("\n ------------------")

# add member function call
def handle_add_member():
    found = False
    member_id = input("Enter member_id:")
    if not member_id:
        print("❌ Member ID is required!")
    else:
        for i in members:
            if i['member_id'] == member_id:
                found = True
                break
        if found:
            print("❌ Error: Id already Exist! Please use different Id!")
        else:
            name = input("Enter your name:")
            if not name:
                print("❌ Name is required!")
            else:
                phone = input("Enter your phone:")
                if not phone:
                    print("❌ Phone is required!")
                else:
                    address = input("Enter your address:")
                    joining_date = input("Enter Joining Date(dd-mm-yyyy):")
                    if not joining_date:
                        print("❌ Joining Date is required!")
                    else:
                        # add member function call
                        add_member(
                            member_id,
                            name,
                            phone,
                            address,
                            joining_date
                        )
# Update phone function
def handle_update_phone():
    search_id = input("Enter Member ID to Update Phone:")
    if not search_id:
        print("❌ Member ID is required!")
    else:
        new_phone = input("Enter new phone number:")
        found = False
        for s in members:
            if s['member_id'] == search_id:
                s['phone'] = new_phone
                save_members()
                found = True
                print("✅ Updated Successfully!")
                break
        if not found:
            print("❌ Member ID not found!")

# delete member function
def handle_delete_member():
    search_id = input("Enter Member ID to Delete:")
    if not search_id:
        print("❌ Member ID is required!")
    else:
        found = False
        for s in members:
            if s['member_id'] == search_id:
                members.remove(s)
                save_members()
                found = True
                print("✅ Deleted Successfully!")
                break
        if not found:
            print("❌ Member ID not found!")

