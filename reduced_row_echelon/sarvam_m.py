n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

pivot_row = 0
for pivot_col in range(m + 1):
    if pivot_row >= n:
        break
    found = -1
    for r in range(pivot_row, n):
        if matrix[r][pivot_col] == 1:
            found = r
            break
    if found == -1:
        continue
    matrix[pivot_row], matrix[found] = matrix[found], matrix[pivot_row]
    for r in range(pivot_row + 1, n):
        if matrix[r][pivot_col] == 1:
            for c in range(pivot_col, m + 1):
                matrix[r][c] ^= matrix[pivot_row][c]
    pivot_row += 1

rank = 0
for row in matrix:
    if any(row):
        rank += 1
print(rank)