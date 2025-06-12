def gauss_jordan_elimination(matrix):
    def find_pivot(matrix, row, col):
        for i in range(row, len(matrix)):
            if matrix[i][col] == 1:
                return i
        return -1

    def swap_rows(matrix, row1, row2):
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

    def xor_rows(matrix, row1, row2):
        matrix[row1] = [matrix[row1][i] ^ matrix[row2][i] for i in range(len(matrix[row1]))]

    rows = len(matrix)
    cols = len(matrix[0])
    rank = 0

    for col in range(cols):
        pivot_row = find_pivot(matrix, rank, col)
        if pivot_row != -1:
            if pivot_row != rank:
                swap_rows(matrix, pivot_row, rank)
            for row in range(rank + 1, rows):
                if matrix[row][col] == 1:
                    xor_rows(matrix, row, rank)
            rank += 1

    return rank

def matrix_rank_gf2():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    matrix = []
    index = 2
    for i in range(N):
        row = [int(data[index + j]) for j in range(M + 1)]
        matrix.append(row)
        index += M + 1
    rank = gauss_jordan_elimination(matrix)
    print(rank)

matrix_rank_gf2()