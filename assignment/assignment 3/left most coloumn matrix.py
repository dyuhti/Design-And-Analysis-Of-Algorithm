def get(matrix, row, col):
    return matrix[row][col]


def dimensions(matrix):
    return [len(matrix), len(matrix[0])]


def leftMostColumnWithOne(matrix):
    rows, cols = dimensions(matrix)
    current_row = 0
    current_col = cols - 1
    leftmost_col = -1

    while current_row < rows and current_col >= 0:
        if get(matrix, current_row, current_col) == 1:
            leftmost_col = current_col
            current_col -= 1
        else:
            current_row += 1

    return leftmost_col


# Example usage
matrix = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 0]
]

result = leftMostColumnWithOne(matrix)
print(result)  # Output: 1
