import math

board = [" "] * 9
WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]


def print_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i + 3]))
        if i < 6:
            print("---+---+---")
    print()


def check_winner(b):
    for a, c, d in WIN_LINES:
        if b[a] == b[c] == b[d] and b[a] != " ":
            return b[a]
    return None


def minimax(b, is_ai_turn, alpha, beta):
    # AI is "O" (wants high score), Human is "X" (wants low score)
    winner = check_winner(b)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if " " not in b:
        return 0

    if is_ai_turn:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False, alpha, beta)
                b[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:  # alpha-beta pruning
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True, alpha, beta)
                b[i] = " "
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:  # alpha-beta pruning
                    break
        return best


def ai_move():
    best_score = -math.inf
    best_pos = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_pos = i
    board[best_pos] = "O"


def play_game():
    global board
    board = [" "] * 9
    print("Tic-Tac-Toe: You are X, AI is O.")
    print("Positions are numbered 1 to 9:")
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9")

    while True:
        # Human turn
        move = input("Your move (1-9): ")
        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Please enter a number from 1 to 9.")
            continue
        pos = int(move) - 1
        if board[pos] != " ":
            print("That place is already taken. Try another.")
            continue
        board[pos] = "X"
        print_board()

        if check_winner(board) == "X":
            print("You win!")
            return
        if " " not in board:
            print("It's a draw!")
            return

        # AI turn
        print("AI is thinking...")
        ai_move()
        print_board()

        if check_winner(board) == "O":
            print("AI wins!")
            return
        if " " not in board:
            print("It's a draw!")
            return


while True:
    play_game()
    again = input("Play again? (yes/no): ").lower().strip()
    if again != "yes":
        print("Thanks for playing. Bye!")
        break