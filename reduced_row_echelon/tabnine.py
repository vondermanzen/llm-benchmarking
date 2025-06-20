def matrix_rank(matrix):
    n, m = len(matrix), len(matrix[0])
    rank = 0

    for col in range(m):
        # Find the pivot row
        pivot_row = rank
        while pivot_row < n and matrix[pivot_row][col] == 0:
            pivot_row += 1

        # Swap pivot row with current row
        if pivot_row != rank:
            matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]

        # Perform row operations to make the pivot element 1
        if matrix[rank][col] == 1:
            for row in range(n):
                if row != rank and matrix[row][col] == 1:
                    matrix[row] = [a ^ b for a, b in zip(matrix[row], matrix[rank])]

        rank += 1

    return rank

# Read input
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Compute rank
rank = matrix_rank(matrix)
print(rank)