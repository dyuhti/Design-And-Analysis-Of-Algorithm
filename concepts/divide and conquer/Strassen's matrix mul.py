def matrix_addition(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrix_subtraction(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def split_matrix(A):
    n = len(A)
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return A11, A12, A21, A22

def strassen_multiply(A, B):
    n = len(A)

    # Base case: If the matrices are 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Split matrices into quarters
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Recursive steps
    P1 = strassen_multiply(matrix_addition(A11, A22), matrix_addition(B11, B22))
    P2 = strassen_multiply(matrix_addition(A21, A22), B11)
    P3 = strassen_multiply(A11, matrix_subtraction(B12, B22))
    P4 = strassen_multiply(A22, matrix_subtraction(B21, B11))
    P5 = strassen_multiply(matrix_addition(A11, A12), B22)
    P6 = strassen_multiply(matrix_subtraction(A21, A11), matrix_addition(B11, B12))
    P7 = strassen_multiply(matrix_subtraction(A12, A22), matrix_addition(B21, B22))

    # Calculate result submatrices
    C11 = matrix_addition(matrix_subtraction(matrix_addition(P1, P4), P5), P7)
    C12 = matrix_addition(P3, P5)
    C21 = matrix_addition(P2, P4)
    C22 = matrix_addition(matrix_subtraction(matrix_addition(P1, P3), P2), P6)

    # Combine result submatrices into the final matrix
    result = [[0] * n for _ in range(n)]
    for i in range(n//2):
        for j in range(n//2):
            result[i][j] = C11[i][j]
            result[i][j + n//2] = C12[i][j]
            result[i + n//2][j] = C21[i][j]
            result[i + n//2][j + n//2] = C22[i][j]

    return result

# Example usage:
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

B = [[17, 18, 19, 20],
     [21, 22, 23, 24],
     [25, 26, 27, 28],
     [29, 30, 31, 32]]

C = strassen_multiply(A, B)
for row in C:
    print(row)
