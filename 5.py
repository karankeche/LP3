def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(board, row, n):
    # Base condition: all queens placed
    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'   # place queen
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = '.'   # backtrack

    return False

# ---- Main Program ----
n = 4  # You can change this to any N
board = [['.' for _ in range(n)] for _ in range(n)]

# Place the first Queen manually (for example, at row 0, col 1)
board[0][1] = 'Q'

# Solve for remaining queens
if not solve_nqueens(board, 1, n):
    print("No solution found.")
