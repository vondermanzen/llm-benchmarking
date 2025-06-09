def matrix_rank_gf2():
    # Read input
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # Perform Gaussian elimination over GF(2)
    rank = 0
    for col in range(M + 1):  # Include augmented column
        # Find pivot row
        pivot_row = -1
        for row in range(rank, N):
            if matrix[row][col] == 1:
                pivot_row = row
                break
        
        if pivot_row == -1:
            continue
            
        # Swap pivot row with current rank row
        if pivot_row != rank:
            matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
        
        # Eliminate column
        for row in range(N):
            if row != rank and matrix[row][col] == 1:
                for j in range(col, M + 1):
                    matrix[row][j] = (matrix[row][j] + matrix[rank][j]) % 2
        
        rank += 1
        
        # If we've processed all rows, break
        if rank >= N:
            break
    
    # Count non-zero rows
    final_rank = sum(1 for row in matrix if any(row))
    
    return final_rank

# Run the program and print result
print(matrix_rank_gf2())