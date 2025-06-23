def matrix_rank_GF2(matrix):
    def pivot_row(i, j):
        for k in range(i, len(matrix)):
            if matrix[k][j] == 1:
                return k
        return -1

    def swap_rows(i, j):
        matrix[i], matrix[j] = matrix[j], matrix[i]

    def add_rows(i, j):
        for k in range(len(matrix[0])):
            matrix[j][k] = (matrix[j][k] + matrix[i][k]) % 2

    rank = 0
    for j in range(len(matrix[0]) - 1):
        pivot = pivot_row(rank, j)
        if pivot == -1:
            continue
        swap_rows(rank, pivot)
        for i in range(rank + 1, len(matrix)):
            add_rows(rank, i)
        rank += 1

    return rank

# Reading input
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# Computing and printing rank
print(matrix_rank_GF2(matrix))