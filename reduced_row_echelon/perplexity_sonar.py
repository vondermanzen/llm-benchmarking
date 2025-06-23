def gf2_rank(matrix, n, m):
    rank = 0
    for col in range(m+1):
        pivot = -1
        for row in range(rank, n):
            if matrix[row][col] == 1:
                pivot = row
                break
        if pivot == -1:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        for row in range(n):
            if row != rank and matrix[row][col] == 1:
                for c in range(col, m+1):
                    matrix[row][c] ^= matrix[rank][c]
        rank += 1
        if rank == n:
            break
    return rank

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(gf2_rank(matrix, n, m))