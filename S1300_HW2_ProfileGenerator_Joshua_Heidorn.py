# Ask the user for input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")
hobby = input("Enter your favorite hobby: ")

# Convert names to title case
first_name = first_name.title()
last_name = last_name.title()

# Convert birth year to integer and calculate age
birth_year = int(birth_year)
current_year = 2026
age = current_year - birth_year

# Create decorative borders
top_border = "=" * 36
middle_border = "-" * 36

# Display the formatted profile card
print(top_border)
print("USER PROFILE CARD")
print(top_border)
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Hobby: {hobby.title()}")
print(middle_border)
print("Thank you for creating your profile!")
print(top_border)