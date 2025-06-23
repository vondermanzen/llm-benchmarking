def binary_rank(N, M, matrix):
    rank = 0
    p = 2
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        if matrix[i][n - 1] == 1:
            rank += 1
            for k in range(i + 1, m):
                if matrix[k][n - 1] == 0:
                    matrix[k] = [a - b for a, b in zip(matrix[k], matrix[i])]
    for i in range(m):
        if matrix[i][n - 1] == 0:
            for k in range(i + 1, m):
                if matrix[k][n - 1] == 1:
                    matrix[k] = [a - b for a, b in zip(matrix[k], matrix[i])]
                    break
    for i in range(m):
        if matrix[i][n - 1] == 1:
            for j in range(n - 1):
                if matrix[i][j] == 1:
                    for k in range(i + 1, m):
                        matrix[k][j] = matrix[k][j] + matrix[k][i] % p
    for i in range(m):
        if all(a == 0 for a in matrix[i]):
            return 'Error: No solution'
        row = [a % p for a in matrix[i]]
        if i < rank:
            if row[n - 1] == 1:
                return rank
            else:
                rank += 1
        else:
            if row[n - 1] == 1:
                return rank
            else:
                return 'Error: Multiple solutions'

N, M = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]
print(binary_rank(N, M, matrix))