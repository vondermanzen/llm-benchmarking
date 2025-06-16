import sys

def gf2_rank(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rank = 0

    for col in range(m):
        pivot_row = None
        for row in range(rank, n):
            if matrix[row][col] == 1:
                pivot_row = row
                break

        if pivot_row is None:
            continue

        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]

        for row in range(n):
            if row != rank and matrix[row][col] == 1:
                for c in range(m):
                    matrix[row][c] ^= matrix[rank][c]

        rank += 1

    return rank

def main():
    input = sys.stdin.read
    data = input().splitlines()
    n, m = map(int, data[0].split())
    matrix = [list(map(int, line.split())) for line in data[1:n+1]]
    print(gf2_rank(matrix))

if __name__ == "__main__":
    main()
