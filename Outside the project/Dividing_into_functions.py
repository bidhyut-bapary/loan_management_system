# Before
while True:
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        print(f"{name} is {age} years old")


# After

def handle_add_person():
    name = input("Name: ")
    age = input("Age: ")
    print(f"{name} is {age} years old")

while True:
    choice = input("Choice: ")
    if choice == "1":
        handle_add_person()