def gauss_elimination(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rank = 0

    for col in range(m):
        pivot_row = rank
        while pivot_row < n and matrix[pivot_row][col] == 0:
            pivot_row += 1

        if pivot_row == n:
            continue

        if pivot_row != rank:
            matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]

        for i in range(rank + 1, n):
            if matrix[i][col] == 1:
                for j in range(col, m):
                    matrix[i][j] ^= matrix[rank][j]

        rank += 1

    return rank

def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    rank = gauss_elimination(matrix)
    print(rank)

if __name__ == "__main__":
    main()