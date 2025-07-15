import math

# Constants
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    print()
    for row in board:
        print('|'.join(row))
        print('-' * 5)
    print()

def is_moves_left(board):
    return any(EMPTY in row for row in board)

def evaluate(board):
    # Rows, columns, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == AI:
                return +10
            elif board[i][0] == HUMAN:
                return -10

        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == AI:
                return +10
            elif board[0][i] == HUMAN:
                return -10

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == AI:
            return +10
        elif board[0][0] == HUMAN:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == AI:
            return +10
        elif board[0][2] == HUMAN:
            return -10

    return 0

def minimax(board, depth, is_max, alpha=-math.inf, beta=math.inf, use_ab=True):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    value = minimax(board, depth + 1, False, alpha, beta, use_ab)
                    board[i][j] = EMPTY
                    best = max(best, value)
                    if use_ab:
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    value = minimax(board, depth + 1, True, alpha, beta, use_ab)
                    board[i][j] = EMPTY
                    best = min(best, value)
                    if use_ab:
                        beta = min(beta, best)
                        if beta <= alpha:
                            break
        return best

def find_best_move(board, use_ab=True):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False, use_ab=use_ab)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def is_game_over(board):
    score = evaluate(board)
    if score == 10:
        print("AI wins!")
        return True
    elif score == -10:
        print("You win!")
        return True
    elif not is_moves_left(board):
        print("It's a draw!")
        return True
    return False

def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', AI is 'O'")
    print_board(board)

    while True:
        # Human Move
        while True:
            try:
                move = input("Enter your move (row and column: 0 2): ")
                row, col = map(int, move.split())
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    break
                else:
                    print("Cell is already occupied.")
            except:
                print("Invalid input. Try again.")
        print_board(board)
        if is_game_over(board):
            break

        # AI Move
        print("AI is making a move...")
        row, col = find_best_move(board)
        board[row][col] = AI
        print_board(board)
        if is_game_over(board):
            break

if __name__ == "__main__":
    play_game()
