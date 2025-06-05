def matrix_rank_gf2(matrix):
    """
    Compute the rank of a matrix over GF(2) using Gaussian elimination.
    
    Args:
        matrix (list): List of lists representing the augmented matrix
        
    Returns:
        int: Rank of the matrix
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a copy to avoid modifying the original matrix
    mat = [row[:] for row in matrix]
    
    rank = 0
    col = 0
    
    # Gaussian elimination over GF(2)
    for col in range(cols):
        # Find pivot row (first row with 1 in current column)
        pivot_row = -1
        for row in range(rank, rows):
            if mat[row][col] == 1:
                pivot_row = row
                break
        
        # If no pivot found, move to next column
        if pivot_row == -1:
            continue
        
        # Swap current row with pivot row
        if pivot_row != rank:
            mat[rank], mat[pivot_row] = mat[pivot_row], mat[rank]
        
        # Eliminate all other 1s in this column (both above and below)
        for row in range(rows):
            if row != rank and mat[row][col] == 1:
                # XOR the pivot row with current row (mod 2 addition)
                for c in range(cols):
                    mat[row][c] ^= mat[rank][c]
        
        rank += 1
    
    return rank

def main():
    # Read input
    n, m = map(int, input().split())
    
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Calculate and output the rank
    rank = matrix_rank_gf2(matrix)
    print(rank)

if __name__ == "__main__":
    main()