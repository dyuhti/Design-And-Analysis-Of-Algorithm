def is_safe(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve(board, col + 1):
                return True
            board[i][col] = 0

    return False


def solve_n(n):
    board = [[0] * n for _ in range(n)]
    if not solve(board, 0):
        print(f"No solution exists")
        return False
    print(f"Solution:")
    for row in board:
        print(row)

    return True

n = 5
solve_n(n)
