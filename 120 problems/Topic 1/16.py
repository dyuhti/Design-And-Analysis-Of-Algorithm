def gameOfLife(board):
    if not board:
        return

    m = len(board)
    n = len(board[0])

    # Define directions for 8 neighbors (horizontal, vertical, diagonal)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Create a new board to store the next state
    new_board = [[0] * n for _ in range(m)]

    # Function to count live neighbors
    def count_live_neighbors(row, col):
        count = 0
        for d in directions:
            nr, nc = row + d[0], col + d[1]
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 1:
                count += 1
        return count

    # Iterate through each cell in the board
    for i in range(m):
        for j in range(n):
            live_neighbors = count_live_neighbors(i, j)

            # Apply the rules of the game
            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0

    # Update the original board with the new state
    for i in range(m):
        for j in range(n):
            board[i][j] = new_board[i][j]


# Example usage:
board1 = [[0, 1, 0], [0, 0, 1], [1,1, 1], [0, 0, 0]]
gameOfLife(board1)
print(board1)  # Output: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

board2 = [[1, 1], [1, 0]]
gameOfLife(board2)
print(board2)  # Output: [[1, 1], [1, 1]]
