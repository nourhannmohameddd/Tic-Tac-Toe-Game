board = [" " for _ in range(9)]  #Board list 3x3

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
    print()

# Function to check for a winner
def check_winner():
    # All possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]  
    return None

# Function to check if the board is full
def is_full():
    return " " not in board

# Minimax Algorithm
def minimax(is_maximizing):
    winner = check_winner()
    if winner == "X":  # Maximizing player
        return 1
    elif winner == "O":  # Minimizing player
        return -1
    elif is_full():  # Tie
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  # Maximizing player's move
                score = minimax(False)
                board[i] = " "  # Undo the move
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  # Minimizing player's move
                score = minimax(True)
                board[i] = " "  # Undo the move
                best_score = min(best_score, score)
        return best_score

# Function to find the best move
def find_best_move():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"  # Maximizing player's move
            score = minimax(False)
            board[i] = " "  # Undo the move
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    while True:
        # Human player's turn (O)
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = "O"
                    break
                else:
                    print("Invalid move! Try again.")
            except (IndexError, ValueError):
                 print("Please enter a valid number between 1 and 9.")
        print_board()

        # Check if human player wins
        if check_winner() == "O":
            print("You win!")
            break
        elif is_full():
            print("It's a tie!")
            break 

        # Computer's turn (X)
        print("Computer's turn...")
        best_move = find_best_move()
        board[best_move] = "X"
        print_board()

        # Check if computer wins
        if check_winner() == "X":
            print("Computer wins!")
            break
        elif is_full():
            print("It's a tie!")
            break

# Run the game
play_game()

# import tkinter as tk

# board = [" " for _ in range(9)]  # Board list 3x3

# # Function to check for a winner
# def check_winner():
#     winning_combinations = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
#         [0, 4, 8], [2, 4, 6]             # Diagonals
#     ]
#     for combo in winning_combinations:
#         if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
#             return board[combo[0]]
#     return None

# # Function to check if the board is full
# def is_full():
#     return " " not in board

# # Minimax Algorithm
# def minimax(is_maximizing):
#     winner = check_winner()
#     if winner == "X":  # Maximizing player
#         return 1
#     elif winner == "O":  # Minimizing player
#         return -1
#     elif is_full():  # Tie
#         return 0

#     if is_maximizing:
#         best_score = -float("inf")
#         for i in range(9):
#             if board[i] == " ":
#                 board[i] = "X"  # Maximizing player's move
#                 score = minimax(False)
#                 board[i] = " "  # Undo the move
#                 best_score = max(best_score, score)
#         return best_score
#     else:
#         best_score = float("inf")
#         for i in range(9):
#             if board[i] == " ":
#                 board[i] = "O"  # Minimizing player's move
#                 score = minimax(True)
#                 board[i] = " "  # Undo the move
#                 best_score = min(best_score, score)
#         return best_score

# # Function to find the best move
# def find_best_move():
#     best_score = -float("inf")
#     best_move = None
#     for i in range(9):
#         if board[i] == " ":
#             board[i] = "X"  # Maximizing player's move
#             score = minimax(False)
#             board[i] = " "  # Undo the move
#             if score > best_score:
#                 best_score = score
#                 best_move = i
#     return best_move

# # Function to update the button text
# def update_button(index, player):
#     board[index] = player
#     buttons[index].config(text=player, state="disabled", fg="black" if player == "X" else "blue", bg="lightgrey")

#     # Check for winner
#     winner = check_winner()
#     if winner == "X":
#         label.config(text="Computer wins!")
#         disable_all_buttons()
#     elif winner == "O":
#         label.config(text="You win!")
#         disable_all_buttons()
#     elif is_full():
#         label.config(text="It's a tie!")
#         disable_all_buttons()

# # Function to disable all buttons (when the game ends)
# def disable_all_buttons():
#     for button in buttons:
#         button.config(state="disabled")

# # Function for the human player's move
# def human_move(index):
#     if board[index] == " ":
#         update_button(index, "O")
#         if check_winner() != "O" and not is_full():
#             computer_move()

# # Function for the computer's move
# def computer_move():
#     best_move = find_best_move()
#     update_button(best_move, "X")

# # Function to reset the board
# def restart_game():
#     global board
#     board = [" " for _ in range(9)]  # Reset the board
#     for button in buttons:
#         button.config(text=" ", state="normal", bg="white")  # Reset button states
#     label.config(text="Your turn!")  # Reset the status label

# # Function to show the game board
# def start_game():
#     welcome_frame.pack_forget()  # Hide the welcome frame
#     game_frame.pack()  # Show the game frame

# # GUI Setup
# root = tk.Tk()
# root.title("Tic-Tac-Toe")

# # Set window size and background color
# root.geometry("400x500")
# root.config(bg="white")

# # Welcome Screen
# welcome_frame = tk.Frame(root, bg="white")
# welcome_label = tk.Label(welcome_frame, text="Welcome to Tic-Tac-Toe!", font=('normal', 20), bg="white")
# welcome_label.pack(pady=50)
# start_button = tk.Button(welcome_frame, text="Start Game", font=('normal', 15), command=start_game)
# start_button.pack(pady=20)
# welcome_frame.pack()

# # Game Screen
# game_frame = tk.Frame(root, bg="white")

# # Create a label to display the status
# label = tk.Label(game_frame, text="Your turn!", font=('normal', 15), bg="white")
# label.grid(row=3, column=0, columnspan=3)

# # Create buttons for the Tic-Tac-Toe grid
# buttons = []
# for i in range(9):
#     button = tk.Button(game_frame, text=" ", width=10, height=3, font=('normal', 20), bd=2,
#                        relief="solid", command=lambda i=i: human_move(i))
#     button.grid(row=i//3, column=i%3, padx=5, pady=5)
#     buttons.append(button)

# # Add Restart button
# restart_button = tk.Button(game_frame, text="Restart", font=('normal', 15), bg="red", fg="white", command=restart_game)
# restart_button.grid(row=4, column=0, columnspan=3, pady=10)

# root.mainloop()
