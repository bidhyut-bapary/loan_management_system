import json

students = [
    {"name": "Karim", "age": 20},
    {"name": "Rahim", "age": 22}
]

# Save করা (Python data → JSON file)
with open("students.json", "w") as file:
    json.dump(students, file)

# Load করা (JSON file → Python data)
with open("students.json", "r") as file:
    loaded_students = json.load(file)

print(loaded_students)
