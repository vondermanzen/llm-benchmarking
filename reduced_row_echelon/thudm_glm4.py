def compute_rank():
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    rank = 0
    for col in range(M + 1):
        if rank >= N:
            break
        # Find pivot row
        pivot_row = -1
        for row in range(rank, N):
            if matrix[row][col] == 1:
                pivot_row = row
                break
        if pivot_row == -1:
            continue
        # Swap current row with pivot row
        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
        # Eliminate this column in other rows
        for row in range(N):
            if row != rank and matrix[row][col] == 1:
                for c in range(col, M + 1):
                    matrix[row][c] ^= matrix[rank][c]
        rank += 1
    print(rank)

compute_rank()