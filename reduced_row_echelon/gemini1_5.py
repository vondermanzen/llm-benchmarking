def solve():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    rank = 0
    col = 0
    for row in range(n):
        while col < m + 1 and all(matrix[i][col] == 0 for i in range(row, n)):
            col += 1
        if col == m + 1:
            break

        pivot_row = row
        for i in range(row + 1, n):
            if matrix[i][col] == 1:
                pivot_row = i
                break
        matrix[row], matrix[pivot_row] = matrix[pivot_row], matrix[row]

        for i in range(n):
            if i != row and matrix[i][col] == 1:
                for j in range(col, m + 1):
                    matrix[i][j] = (matrix[i][j] + matrix[row][j]) % 2
        rank += 1


    print(rank)

solve()