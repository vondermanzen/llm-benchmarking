import sys

def solve():
    N, M = map(int, sys.stdin.readline().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    rank = 0
    pivot_row = 0
    for j in range(M + 1):  # Iterate through columns
        if pivot_row >= N:
            break
        
        i = pivot_row
        while i < N and matrix[i][j] == 0:
            i += 1
        
        if i < N:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
            
            for k in range(N):
                if k != pivot_row and matrix[k][j] == 1:
                    for l in range(j, M + 1):
                        matrix[k][l] ^= matrix[pivot_row][l]
            
            pivot_row += 1

    # The rank is the number of non-zero rows after reduction
    # In this implementation, pivot_row directly gives the rank
    # as it counts the number of pivots found.
    print(pivot_row)

solve()