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
    print(f"Member added: {name}")


def view_members():
    for member in members:
        print(f"ID: {member['member_id']} | Name: {member['name']} | Phone: {member['phone']} | Status: {member['status']}")

add_member(1, "Biswajit", "01788568379", "Barishal", "12-10-2026", "active")
add_member(2, "Rahim", "01711223344", "Dhaka", "15-10-2026")

print("\n--- Member List ---")
view_members()
