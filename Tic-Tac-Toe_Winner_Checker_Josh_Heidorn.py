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