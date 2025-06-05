def compute_rank(N, M, matrix):
    rank = 0
    for col in range(M + 1):  # include augmented column
        # Find the pivot row
        pivot = -1
        for row in range(rank, N):
            if matrix[row][col] == 1:
                pivot = row
                break
        if pivot == -1:
            continue
        # Swap the current row with the pivot row
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        # Eliminate this column in all other rows
        for row in range(N):
            if row != rank and matrix[row][col] == 1:
                # XOR the entire row with the pivot row
                matrix[row] = [(matrix[row][i] + matrix[rank][i]) % 2 for i in range(M + 1)]
        rank += 1
    return rank

# Read input
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Compute rank
rank = compute_rank(N, M, matrix)
print(rank)