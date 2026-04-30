# Campus Café Menu

print("==============================")
print(" CAMPUS CAFÉ ORDER SYSTEM")
print("==============================")
print(" 1. Coffee - $3.50")
print(" 2. Sandwich - $6.00")
print(" 3. Salad - $5.50")
print(" 4. Combo - $8.00")
print(" 5. Exit")
print("==============================")

choice = input("Enter your choice (1-5): ").strip()

if choice == "5":
    print("Goodbye!")
else:
    item = ""
    unit_price = 0.00

    if choice == "1":
        size = input("Choose size: Small, Medium, or Large: ").strip().lower()

        if size == "medium":
            item = "Coffee - Medium"
            unit_price = 4.50
        elif size == "large":
            item = "Coffee - Large"
            unit_price = 5.50
        elif size == "small":
            item = "Coffee - Small"
            unit_price = 3.50
        else:
            print("Invalid size. Defaulting to Small.")
            item = "Coffee - Small"
            unit_price = 3.50

    elif choice == "2":
        cheese = input("Add cheese? (yes/no): ").strip().lower()

        if cheese == "yes":
            item = "Sandwich + Cheese"
            unit_price = 6.75
        else:
            item = "Sandwich"
            unit_price = 6.00

    elif choice == "3":
        dressing = input("Choose dressing: ranch, italian, vinaigrette, or none: ").strip().lower()

        if dressing == "ranch" or dressing == "italian" or dressing == "vinaigrette" or dressing == "none":
            item = f"Salad with {dressing}"
        else:
            print("Invalid dressing. Defaulting to none.")
            item = "Salad with none"

        unit_price = 5.50

    elif choice == "4":
        size = input("Choose coffee size: Small, Medium, or Large: ").strip().lower()
        cheese = input("Add cheese to sandwich? (yes/no): ").strip().lower()

        if size == "medium":
            item = "Combo with Medium Coffee"
            unit_price = 9.00
        elif size == "large":
            item = "Combo with Large Coffee"
            unit_price = 10.00
        elif size == "small":
            item = "Combo with Small Coffee"
            unit_price = 8.00
        else:
            print("Invalid size. Defaulting to Small.")
            item = "Combo with Small Coffee"
            unit_price = 8.00

        if cheese == "yes":
            item += " + Cheese"
            unit_price += 0.75

    else:
        print("Invalid menu choice.")
        item = None

    if item is not None:
        name = input("Enter your name: ").strip()

        if name == "":
            print("Error: Name cannot be empty.")
        else:
            try:
                quantity = int(input("How many? "))

                if quantity <= 0:
                    print("Error: Quantity must be positive.")
                else:
                    subtotal = unit_price * quantity
                    tax = subtotal * 0.07
                    total = subtotal + tax

                    print("==============================")
                    print(" ORDER RECEIPT")
                    print("==============================")
                    print(f" Customer: {name}")
                    print(f" Item: {item}")
                    print(f" Quantity: {quantity}")
                    print(f" Unit Price: ${unit_price:.2f}")
                    print(f" Subtotal: ${subtotal:.2f}")
                    print(f" Tax (7%): ${tax:.2f}")
                    print(f" Total: ${total:.2f}")
                    print("==============================")
                    print("Thank you for your order!")

            except ValueError:
                print("Error: Quantity must be a valid integer.")