def solve():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    rank = 0
    row = 0
    for col in range(m):
        pivot_row = row
        while pivot_row < n and matrix[pivot_row][col] == 0:
            pivot_row += 1

        if pivot_row < n:
            matrix[row], matrix[pivot_row] = matrix[pivot_row], matrix[row]
            rank += 1

            for i in range(n):
                if i != row and matrix[i][col] == 1:
                    for j in range(m + 1):
                        matrix[i][j] = (matrix[i][j] - matrix[row][j]) % 2

            row += 1

    print(rank)

solve()