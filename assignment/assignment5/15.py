def diagonalSort(mat):
    m, n = len(mat), len(mat[0])
    diagonals = {}

    for i in range(m):
        for j in range(n):
            if (i - j) not in diagonals:
                diagonals[i - j] = []
            diagonals[i - j].append(mat[i][j])

    for key in diagonals:
        diagonals[key].sort()

    for i in range(m):
        for j in range(n):
            mat[i][j] = diagonals[i - j].pop(0)
    return mat


mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
print("Output:", diagonalSort(mat))
