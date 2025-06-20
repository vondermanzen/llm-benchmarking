def row_echelon_form_gf2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rank = 0
    lead = 0
    
    for r in range(rows):
        if lead >= cols:
            break
            
        # Find pivot
        i = r
        while i < rows and matrix[i][lead] == 0:
            i += 1
            
        if i == rows:
            lead += 1
            continue
            
        # Swap rows if needed
        if i != r:
            matrix[r], matrix[i] = matrix[i], matrix[r]
        
        # Eliminate below
        for i in range(r + 1, rows):
            if matrix[i][lead] == 1:
                # XOR operation (addition in GF(2))
                for j in range(lead, cols):
                    matrix[i][j] = (matrix[i][j] + matrix[r][j]) % 2
                    
        lead += 1
        rank += 1
    
    # Back-substitution and count non-zero rows
    rank = 0
    for i in range(rows):
        if any(matrix[i]):
            rank += 1
            
    return rank

def main():
    try:
        # Read dimensions
        N, M = map(int, input().strip().split())
        
        # Validate input constraints
        if not (1 <= N <= 1000 and 1 <= M <= 1000):
            print("Matrix dimensions must be between 1 and 1000")
            return
        
        # Read matrix
        matrix = []
        for _ in range(N):
            row = list(map(int, input().strip().split()))
            
            # Validate row length and binary values
            if len(row) != M + 1:
                print(f"Each row must contain exactly {M + 1} values")
                return
            if not all(x in (0, 1) for x in row):
                print("All values must be binary (0 or 1)")
                return
                
            matrix.append(row)
        
        # Calculate and print rank
        rank = row_echelon_form_gf2(matrix)
        print(rank)
        
    except ValueError:
        print("Invalid input format. Please enter valid binary values.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
