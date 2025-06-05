def matrix_rank(matrix):
    # Get dimensions
    n = len(matrix)
    m = len(matrix[0])
    
    # Perform Gaussian elimination over GF(2)
    rank = 0
    for col in range(m):
        # Find pivot row
        pivot_row = None
        for row in range(rank, n):
            if matrix[row][col] == 1:
                pivot_row = row
                break
        
        if pivot_row is None:
            continue
            
        # Swap pivot row with current rank row
        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
        
        # Eliminate 1s below pivot
        for row in range(rank + 1, n):
            if matrix[row][col] == 1:
                for c in range(col, m):
                    matrix[row][c] ^= matrix[rank][c]
        
        rank += 1
    
    return rank

def main():
    # Read input
    N, M = map(int, input().split())
    
    # Read matrix
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Calculate and print rank
    print(matrix_rank(matrix))

if __name__ == "__main__":
    main()
