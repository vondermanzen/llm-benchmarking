import numpy as np

def gf2_rank(matrix):
    rows, cols = matrix.shape
    rank = 0
    for col in range(cols):
        pivot_row = None
        for row in range(rank, rows):
            if matrix[row, col] == 1:
                pivot_row = row
                break
        if pivot_row is not None:
            matrix[rank], matrix[pivot_row] = matrix[pivot_row].copy(), matrix[rank].copy()
            for r in range(rows):
                if r != rank and matrix[r, col] == 1:
                    matrix[r] ^= matrix[rank]
            rank += 1
    return rank

N, M = map(int, input().split())
matrix = np.array([list(map(int, input().split())) for _ in range(N)])

print(gf2_rank(matrix))