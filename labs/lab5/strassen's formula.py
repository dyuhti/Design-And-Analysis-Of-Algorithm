import numpy as np


def add(A, B):
    return np.add(A, B)


def sub(A, B):
    return np.subtract(A, B)


def split(A):
    row, col = A.shape
    row2, col2 = row // 2, col // 2
    return A[:row2, :col2], A[:row2, col2:], A[row2:, :col2], A[row2:, col2:]


def strassen(A, B):
    if len(A) == 1:
        return A * B

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    P1 = strassen(add(A11, A22), add(B11, B22))
    P2 = strassen(add(A21, A22), B11)
    P3 = strassen(A11, sub(B12, B22))
    P4 = strassen(A22, sub(B21, B11))
    P5 = strassen(add(A11, A12), B22)
    P6 = strassen(sub(A21, A11), add(B11, B12))
    P7 = strassen(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(P1, P4), P5), P7)
    C12 = add(P3, P5)
    C21 = add(P2, P4)
    C22 = add(sub(add(P1, P3), P2), P6)

    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    C = np.vstack((top, bottom))

    return C


A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

B = np.array([[17, 18, 19, 20],
              [21, 22, 23, 24],
              [25, 26, 27, 28],
              [29, 30, 31, 32]])

C = strassen(A, B)
print(C)
