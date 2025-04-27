class BinaryMatrix:
    def __init__(self, mat):
        self.mat = mat

    def get(self, row: int, col: int) -> int:
        return self.mat[row][col]

    def dimensions(self) -> list:
        return [len(self.mat), len(self.mat[0])]


def leftMostColumnWithOne(binaryMatrix):
    rows, cols = binaryMatrix.dimensions()
    current_row = 0
    current_col = cols - 1
    leftmost_col_with_one = -1

    # Traverse the matrix from the top-right corner
    while current_row < rows and current_col >= 0:
        if binaryMatrix.get(current_row, current_col) == 1:
            leftmost_col_with_one = current_col
            current_col -= 1  # Move left
        else:
            current_row += 1  # Move down

    return leftmost_col_with_one


# Example usage
# Example 1
mat1 = [[0, 0], [1, 1]]
binaryMatrix1 = BinaryMatrix(mat1)
print(leftMostColumnWithOne(binaryMatrix1))  # Output: 0

# Example 2
mat2 = [[0, 0], [0, 1]]
binaryMatrix2 = BinaryMatrix(mat2)
print(leftMostColumnWithOne(binaryMatrix2))  # Output: 1

# Example 3
mat3 = [[0, 0], [0, 0]]
binaryMatrix3 = BinaryMatrix(mat3)
print(leftMostColumnWithOne(binaryMatrix3))  # Output: -1
