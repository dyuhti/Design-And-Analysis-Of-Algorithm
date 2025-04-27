def is_safe(board, row, col):
    # Check if the queen can be placed at board[row][col]

    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col):
    # Base case: All queens are placed
    if col >= len(board):
        return True

    # Consider this column and try placing queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    return False


def solve_n_queens(n):
    # Initialize the board
    board = [[0] * n for _ in range(n)]

    # Call the helper function to solve N-Queens problem
    if not solve_n_queens_util(board, 0):
        print(f"No solution exists for {n}-Queens problem")
        return False

    # Print the board
    print(f"Solution for {n}-Queens problem:")
    for row in board:
        print(row)

    return True


# Example usage:
n = 8  # Size of the chessboard and number of queens
solve_n_queens(n)
