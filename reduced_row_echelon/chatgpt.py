def gf2_matrix_rank(matrix, n, m_plus_1):
    m = m_plus_1 - 1  # number of variables
    rank = 0
    row = 0

    for col in range(m_plus_1):  # include last column (augmented part)
        pivot = -1
        for i in range(row, n):
            if matrix[i][col]:
                pivot = i
                break

        if pivot == -1:
            continue

        # Swap current row with pivot row
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]

        # Eliminate column values for all rows below and above
        for i in range(n):
            if i != row and matrix[i][col]:
                # XOR operation in GF(2)
                matrix[i] = [a ^ b for a, b in zip(matrix[i], matrix[row])]
        
        row += 1
        rank += 1

    return rank

# Read input
def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    M = int(data[1])
    matrix = []

    idx = 2
    for _ in range(N):
        row = list(map(int, data[idx:idx + M + 1]))
        matrix.append(row)
        idx += M + 1

    rank = gf2_matrix_rank(matrix, N, M + 1)
    print(rank)

if __name__ == "__main__":
    main()
