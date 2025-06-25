import sys


def parse_input():
    data = sys.stdin.read().strip().split()
    if not data:
        return 0, 0, []
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    matrix = []
    for _ in range(N):
        row = [int(next(it)) for _ in range(M + 1)]
        matrix.append(row)
    return N, M, matrix


def gaussian_elimination(matrix, N, M):
    row = 0
    rank = 0
    for col in range(M + 1):
        pivot = None
        for r in range(row, N):
            if matrix[r][col] == 1:
                pivot = r
                break
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        for r in range(N):
            if r != row and matrix[r][col] == 1:
                for c in range(col, M + 1):
                    matrix[r][c] ^= matrix[row][c]
        row += 1
        rank += 1
        if row == N:
            break
    return rank


def main():
    N, M, matrix = parse_input()
    rank = gaussian_elimination(matrix, N, M)
    print(rank)


if __name__ == "__main__":
    main()
