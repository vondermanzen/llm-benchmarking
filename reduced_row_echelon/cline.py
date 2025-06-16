def gaussian_elimination_gf2(matrix):
    """
    Perform Gaussian elimination over GF(2) (binary field) to convert
    the matrix to reduced row echelon form.
    
    Args:
        matrix (list): A list of lists representing the augmented matrix [A|b]
        
    Returns:
        list: The matrix in reduced row echelon form
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Keep track of where the leading 1 is in each row
    lead = 0
    
    for r in range(rows):
        if lead >= cols:
            break
            
        # Find the pivot row
        i = r
        while i < rows and matrix[i][lead] == 0:
            i += 1
            
        if i == rows:
            # No pivot in this column, move to the next column
            lead += 1
            r -= 1  # Stay on the same row
            continue
            
        # Swap rows if needed
        if i != r:
            matrix[r], matrix[i] = matrix[i], matrix[r]
            
        # Eliminate other rows
        for i in range(rows):
            if i != r and matrix[i][lead] == 1:
                # XOR operation (addition modulo 2)
                for j in range(lead, cols):
                    matrix[i][j] = (matrix[i][j] + matrix[r][j]) % 2
                    
        lead += 1
        
    return matrix

def count_non_zero_rows(matrix):
    """
    Count the number of non-zero rows in a matrix.
    
    Args:
        matrix (list): A list of lists representing a matrix
        
    Returns:
        int: The number of non-zero rows
    """
    count = 0
    for row in matrix:
        if any(row):
            count += 1
    return count

def main():
    # Read input
    n, m = map(int, input().split())
    
    # Read the augmented matrix [A|b]
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Perform Gaussian elimination over GF(2)
    rref_matrix = gaussian_elimination_gf2(matrix)
    
    # Count non-zero rows to determine the rank
    rank = count_non_zero_rows(rref_matrix)
    
    # Output the rank
    print(rank)

if __name__ == "__main__":
    main()
