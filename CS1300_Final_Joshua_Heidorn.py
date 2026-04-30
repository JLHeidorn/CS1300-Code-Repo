Problem #1     Compound Interest Calculator


principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
years = int(input("Years: "))

balance = principal

for year in range(1, years + 1):
    balance = balance * (1 + rate / 100)
    print(f"Year {year}: ${balance:.2f}")

interest = balance - principal
print(f"Total interest earned: ${interest:.2f}")



Problem #2        Caesar Cipher Encoder


def caesar_encode(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.islower():
                result += chr((ord(ch) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += ch

    return result


# Tests
print(caesar_encode("Hello, World!", 3))  # Khoor, Zruog!
print(caesar_encode("abc xyz", 2))        # cde zab
print(caesar_encode("Python 3", 5))       # Udymts 3


Problem #3    Matrix Transpose


def transpose(matrix):
    result = []

    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        result.append(new_row)

    return result


# Tests
m1 = [[1, 2, 3],
      [4, 5, 6]]
print(transpose(m1))  

#Expected output [[1, 4], [2, 5], [3, 6]]

m2 = [[1, 2],
      [3, 4],
      [5, 6]]
print(transpose(m2))  

#Expected output is [[1, 3, 5], [2, 4, 6]]

Problem #4    Tic Tac Toe Checker 


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check if full
    for row in board:
        if " " in row:
            return "Ongoing"

    return "Draw"


# Tests
board1 = [["X", "X", "X"],
          ["O", "O", " "],
          [" ", " ", " "]]
print(check_winner(board1))  #Winner is X

board2 = [["X", "O", "X"],
          ["X", "O", " "],
          [" ", "O", "X"]]
print(check_winner(board2))  #Winner is O

board3 = [["X", "O", "X"],
          ["X", "O", "O"],
          ["O", "X", "X"]]
print(check_winner(board3))  # Draw

board4 = [["X", "O", " "],
          [" ", "X", " "],
          [" ", " ", " "]]
print(check_winner(board4))  # Ongoing


#Custom test board

board5 = [["X", "O", "X"],
          ["X", "X", "O"],
          ["O", "X", "X"]]
print(check_winner(board5))   #X will win



Problem #5     Simple Expense Tracker


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
