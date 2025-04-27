def matrix_multiply(matrix1, matrix2):
    # Check dimensions
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # Check if matrices can be multiplied
    if cols1 != rows2:
        print("Cannot multiply the matrices. Invalid dimensions.")
        return None

    # Initialize result matrix
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(rows2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


# Example usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = matrix_multiply(matrix1, matrix2)
if result:
    print("Matrix multiplication result:")
    for row in result:
        print(row)
