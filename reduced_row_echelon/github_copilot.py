def read_matrix():
    import sys
    input_lines = sys.stdin.read().splitlines()
    n, m = map(int, input_lines[0].split())
    matrix = []
    for i in range(1, n+1):
        row = list(map(int, input_lines[i].split()))
        matrix.append(row)
    return matrix, n, m

def gf2_rank(matrix, n, m_aug):
    # Gaussian elimination over GF(2)
    rank = 0
    row = 0
    col = 0
    while row < n and col < m_aug:
        # find a row with a 1 in this column
        sel = -1
        for i in range(row, n):
            if matrix[i][col]:
                sel = i
                break
        if sel == -1:
            # No 1 found in this column, move to next column
            col += 1
            continue
        # swap current row with selected row
        matrix[row], matrix[sel] = matrix[sel], matrix[row]
        # eliminate all other 1's in this column
        for i in range(n):
            if i != row and matrix[i][col]:
                # add current row to this row (XOR)
                for j in range(col, m_aug):
                    matrix[i][j] ^= matrix[row][j]
        row += 1
        col += 1
    # Count non-zero rows
    rank = 0
    for i in range(n):
        if any(matrix[i][j] for j in range(m_aug)):
            rank += 1
    return rank

def main():
    matrix, n, m = read_matrix()
    m_aug = m + 1  # Include augmented column
    rank = gf2_rank(matrix, n, m_aug)
    print(rank)

if __name__ == "__main__":
    main()