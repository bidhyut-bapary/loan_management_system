# --- Test Section ---
a = []   # ← এখানে payment list এর জায়গায় a ব্যবহার করছি

def add_a(x, y, z):
    item = {
        "x": x,   # payment_id এর জায়গায় x
        "y": y,   # loan_id এর জায়গায় y
        "z": z    # payment_amount এর জায়গায় z
    }
    a.append(item)

def get_total_y(y):
    total = 0
    for item in a:
        if item["y"] == y:   # loan_id মিললে যোগ হবে
            total = total + item["z"]
    return total

# --- Test Run ---
add_a(1, "L001", 500)
add_a(2, "L001", 300)
add_a(3, "L002", 200)

print("Total for L001:", get_total_y("L001"))  # → 800
print("Total for L002:", get_total_y("L002"))  # → 200

