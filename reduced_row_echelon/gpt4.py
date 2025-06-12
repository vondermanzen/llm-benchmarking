def matrix_rank(matrix):

    def swap_rows(matrix, row1, row2):
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

    def add_rows(matrix, target_row, added_row):
        matrix[target_row] = [(a + b) % 2 for a, b in zip(matrix[target_row], matrix[added_row])]

    def move_row(matrix, row):
        while row < len(matrix) and matrix[row][row] == 0:
            for r in range(row + 1, len(matrix)):
                if matrix[r][row] == 1:
                    swap_rows(matrix, r, row)
                    break
            else:
                row += 1
        return row

    N = len(matrix)
    M = len(matrix[0])
    
    row = 0
    while row < N:
        row = move_row(matrix, row)
        if row == N:
            break
        for r in range(row + 1, N):
            if matrix[r][row] == 1:
                add_rows(matrix, r, row)
        row += 1

    rank = sum(any(row) for row in matrix)
    return rank

n, m = 3, 3
matrix = [[1, 0, 1, 1],
          [0, 1, 1, 0],
          [1, 1, 0, 1]]
print(matrix_rank(matrix))  # Expected output: 3