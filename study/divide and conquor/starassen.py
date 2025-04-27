def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def subtract_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def split_matrix(M):
    n = len(M)
    mid = n // 2
    return [[M[i][:mid] for i in range(mid)], [M[i][mid:] for i in range(mid)], [M[i + mid][:mid] for i in range(mid)],
            [M[i + mid][mid:] for i in range(mid)]]


def join_matrices(C11, C12, C21, C22):
    n = len(C11)
    return [C11[i] + C12[i] for i in range(n)] + [C21[i] + C22[i] for i in range(n)]


def strassen_multiply(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)
    P1 = strassen_multiply(add_matrix(A11, A22), add_matrix(B11, B22))
    P2 = strassen_multiply(add_matrix(A21, A22), B11)
    P3 = strassen_multiply(A11, subtract_matrix(B12, B22))
    P4 = strassen_multiply(A22, subtract_matrix(B21, B11))
    P5 = strassen_multiply(add_matrix(A11, A12), B22)
    P6 = strassen_multiply(subtract_matrix(A21, A11), add_matrix(B11, B12))
    P7 = strassen_multiply(subtract_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(subtract_matrix(add_matrix(P1, P4), P5), P7)
    C12 = add_matrix(P3, P5)
    C21 = add_matrix(P2, P4)
    C22 = add_matrix(subtract_matrix(add_matrix(P1, P3), P2), P6)

    return join_matrices(C11, C12, C21, C22)


# Example usage:
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
B = [[16, 15, 14, 13],
     [12, 11, 10, 9],
     [8, 7, 6, 5],
     [4, 3, 2, 1]]
result = strassen_multiply(A, B)
print("Resulting matrix:")
for row in result:
    print(row)
