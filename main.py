import random
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def print_board(board):
    for row in board:
        for cell in row:
            if cell == 'X':
                print(Fore.RED + cell, end=' ')
            elif cell == 'O':
                print(Fore.BLUE + cell, end=' ')
            else:
                print(cell, end=' ')
        print()

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    print()
    for row in range(3):
        for col in range(3):
            if col < 2:
                print(f" {board[row][col]} ", end="|")
            else:
                print(f" {board[row][col]} ")
        if row < 2:
            print("---|---|---")
    print()

def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please try again.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] != ' ':
                print("Cell already taken. Please try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def get_ai_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)

def check_winner(board, player):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for condition in win_conditions:
        if all(board[row][col] == player for row, col in condition):
            return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = initialize_board()
    user_choice = input("Choose X or O: ").upper()
    while user_choice not in ['X', 'O']:
        user_choice = input("Invalid choice. Choose X or O: ").upper()

    ai_choice = 'O' if user_choice == 'X' else 'X'
    current_player = user_choice if user_choice == 'X' else ai_choice

    while True:
        display_board(board)
        if current_player == user_choice:
            print("Your turn.")
            row, col = get_user_move(board)
        else:
            print("AI's turn.")
            row, col = get_ai_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"{current_player} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = user_choice if current_player == ai_choice else ai_choice

if __name__ == "__main__":
    main()
