import sys

# Read dimensions
N, M = map(int, input().split())

# Read the augmented matrix
matrix = [list(map(int, input().split())) for _ in range(N)]

rank = 0
row = 0

for col in range(M + 1):  # Include the augmented column
    # Find pivot row
    pivot_row = -1
    for i in range(row, N):
        if matrix[i][col] == 1:
            pivot_row = i
            break

    if pivot_row == -1:
        continue  # No pivot in this column

    # Swap current row with pivot row
    matrix[row], matrix[pivot_row] = matrix[pivot_row], matrix[row]

    # Eliminate below and above
    for i in range(N):
        if i != row and matrix[i][col] == 1:
            for j in range(M + 1):
                matrix[i][j] ^= matrix[row][j]

    row += 1

# Count non-zero rows
for i in range(N):
    if any(matrix[i]):
        rank += 1

print(rank)
