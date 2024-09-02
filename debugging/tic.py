#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the game board.
    
    Args:
        board (list of list of str): The 3x3 Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """
    Checks if there is a winner on the board.
    
    Args:
        board (list of list of str): The 3x3 Tic-Tac-Toe board.
    
    Returns:
        bool: True if there's a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Checks if the board is full.
    
    Args:
        board (list of list of str): The 3x3 Tic-Tac-Toe board.
    
    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Runs the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if row not in range(3) or col not in range(3):
                    print("Please enter a valid row and column between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Please enter valid numbers.")
        
        board[row][col] = player
        
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        player = "O" if player == "X" else "X"

tic_tac_toe()
