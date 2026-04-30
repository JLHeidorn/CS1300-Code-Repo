descriptions = []
amounts = []

while True:
    print("\n1. Add expense")
    print("2. View all expenses")
    print("3. Total spent")
    print("4. Largest expense")
    print("5. Remove expense")
    print("6. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        desc = input("Enter description: ")
        amt = float(input("Enter amount: "))
        if amt >= 0:
            descriptions.append(desc)
            amounts.append(amt)
        else:
            print("Invalid amount.")

    elif choice == "2":
        if not descriptions:
            print("No expenses recorded.")
        else:
            for i in range(len(descriptions)):
                print(f"{i+1}. {descriptions[i]}: ${amounts[i]:.2f}")

    elif choice == "3":
        total = sum(amounts)
        print(f"Total: ${total:.2f}")

    elif choice == "4":
        if not amounts:
            print("No expenses to compare.")
        else:
            max_amt = max(amounts)
            index = amounts.index(max_amt)
            print(f"Largest: {descriptions[index]} (${max_amt:.2f})")

    elif choice == "5":
        num = int(input("Enter expense number to remove: "))
        if 1 <= num <= len(descriptions):
            descriptions.pop(num - 1)
            amounts.pop(num - 1)
        else:
            print("Invalid number.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")