def matrix_rank_gf2(matrix):
    """
    Computes the rank of the augmented matrix over GF(2).
    :param matrix: List of lists, each sublist is a row of the augmented matrix (length M+1)
    :return: Integer rank
    """
    n = len(matrix)
    m = len(matrix[0])  # m = number of variables + 1 (augmented column)
    row = 0
    for col in range(m):
        # Find a row with a 1 in this column at or below 'row'
        sel = -1
        for i in range(row, n):
            if matrix[i][col]:
                sel = i
                break
        if sel == -1:
            continue  # No pivot in this column
        # Swap to the current row
        matrix[row], matrix[sel] = matrix[sel], matrix[row]
        # Eliminate all other 1s in this column
        for i in range(n):
            if i != row and matrix[i][col]:
                # Row i = Row i XOR Row row
                for j in range(col, m):
                    matrix[i][j] ^= matrix[row][j]
        row += 1
        if row == n:
            break
    # Count non-zero rows
    rank = 0
    for i in range(n):
        if any(matrix[i][j] != 0 for j in range(m)):
            rank += 1
    return rank

if __name__ == "__main__":
    import sys
    import threading

    def main():
        N, M = map(int, sys.stdin.readline().split())
        matrix = []
        for _ in range(N):
            row = list(map(int, sys.stdin.readline().split()))
            matrix.append(row)
        print(matrix_rank_gf2(matrix))

    threading.Thread(target=main).start()