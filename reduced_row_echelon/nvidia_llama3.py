def gf2_rank(matrix):
    n, m = len(matrix), len(matrix[0]) - 1
    lead = 0
    rowCount = 0

    for r in range(n):
        if lead >= m:
            return rowCount

        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == n:
                i = r
                lead += 1
                if m == lead:
                    return rowCount

        matrix[r], matrix[i] = matrix[i], matrix[r]

        for i in range(n):
            if i != r and matrix[i][lead] == 1:
                for j in range(m + 1):
                    matrix[i][j] = (matrix[i][j] + matrix[r][j]) % 2

        lead += 1
        rowCount += 1

    return rowCount


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(gf2_rank(matrix))