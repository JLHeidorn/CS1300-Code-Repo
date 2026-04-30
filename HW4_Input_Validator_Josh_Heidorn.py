# Student Profile Input Validator

errors = []

student_id = input("Enter student ID: ").strip()
name = input("Enter full name: ").strip()
age_input = input("Enter age: ").strip()
major = input("Enter major: ").strip().upper()

if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")

if len(student_id) == 0 or not student_id[0].isalpha():
    errors.append("Student ID must start with a letter")

if len(student_id) < 8 or not student_id[1:].isdigit():
    errors.append("Student ID must have 7 digits after the first letter")

if name == "":
    errors.append("Name cannot be empty")
elif len(name) < 2:
    errors.append("Name must be at least 2 characters")

try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except ValueError:
    errors.append("Age must be a valid integer")
    age = None

valid_majors = ["CS", "IT", "CE", "DS"]

if major not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")

if len(errors) == 0:
    print("✓ Profile created successfully!")
    print(f" Student ID: {student_id}")
    print(f" Name: {name}")
    print(f" Age: {age}")
    print(f" Major: {major}")
else:
    print("✗ Profile has errors:")
    for error in errors:
        print(f" - {error}")