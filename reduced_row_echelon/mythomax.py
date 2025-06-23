def matrix_rank(A, b):
    n = len(A)
    m = len(A[0])
    for i in range(m, n+m):
        if A[i] == 0:
            continue
        j = i - m
        while j >= 0 and A[j] == 0:
            j -= m
        if j < 0:
            return i + m
        A[j], A[i] = A[i], A[j]
        b[j], b[i] = b[i] - b[j] * 2, b[j] * 2
    return len(A) + m

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    b = [int(input())] * (N + 1)
    print(matrix_rank(A, b))