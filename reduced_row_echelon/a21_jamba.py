import numpy as np

def gf2_rank(n, m, matrix):
    augmented_matrix = np.array(matrix, dtype=np.int8)
    rank = 0

    for col in range(m):
        pivot_row = None

        for row in range(n):
            if augmented_matrix[row, col] == 1:
                pivot_row = row
                break

        if pivot_row is not None:
            rank += 1
            augmented_matrix[pivot_row, :] ^= augmented_matrix[row, :]

    return rank

# Read input
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# Compute rank
rank = gf2_rank(n, m, matrix)
print(rank)