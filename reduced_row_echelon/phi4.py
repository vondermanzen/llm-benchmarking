def matrix_rank_gf2(matrix):
    N = len(matrix)
    M = len(matrix[0]) - 1

    # Convert matrix to row echelon form
    row = 0
    for col in range(M + 1):
        if row >= N:
            break

        # Find pivot for this column
        pivot = row
        for r in range(row + 1, N):
            if matrix[r][col] == 1:
                pivot = r
                break

        if matrix[pivot][col] == 0:
            continue

        # Swap pivot row with current row
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]

        # Eliminate column entries below pivot
        for r in range(row + 1, N):
            if matrix[r][col] == 1:
                for c in range(col, M + 1):
                    matrix[r][c] ^= matrix[row][c]

        row += 1

    # Convert to reduced row echelon form
    for row in range(N - 1, -1, -1):
        pivot = -1
        for col in range(M + 1):
            if matrix[row][col] == 1:
                pivot = col
                break

        if pivot == -1 or pivot == M:
            continue

        # Eliminate column entries above pivot
        for r in range(row - 1, -1, -1):
            if matrix[r][pivot] == 1:
                for c in range(pivot, M + 1):
                    matrix[r][c] ^= matrix[row][c]

    # Count non-zero rows
    rank = 0
    for r in range(N):
        if any(matrix[r]):
            rank += 1

    return rank

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()

N = int(data[0])
M = int(data[1])

matrix = []
index = 2
for _ in range(N):
    row = list(map(int, data[index:index + M + 1]))
    matrix.append(row)
    index += M + 1

# Compute and print the rank
print(matrix_rank_gf2(matrix))