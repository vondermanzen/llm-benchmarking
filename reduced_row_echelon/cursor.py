def gf2_rank(matrix, n, m):
    rank = 0
    row = 0
    for col in range(m + 1):
        pivot = -1
        for i in range(row, n):
            if matrix[i][col]:
                pivot = i
                break
        if pivot == -1:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        for i in range(n):
            if i != row and matrix[i][col]:
                for j in range(col, m + 1):
                    matrix[i][j] ^= matrix[row][j]
        row += 1
    # Count non-zero rows
    for i in range(n):
        if any(matrix[i][j] for j in range(m + 1)):
            rank += 1
    return rank

if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(gf2_rank(matrix, N, M))
