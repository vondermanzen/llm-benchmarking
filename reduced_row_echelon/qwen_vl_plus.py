def gaussian_elimination(matrix):
    n_rows, m_cols = len(matrix), max(len(row) for row in matrix)+1
    
    def swap_rows(i, j):
        if i != j:
            temp_row = list(matrix[i])
            matrix[i] = matrix[j]
            matrix[j] = temp_row
            
    def pivot_element(r, c=0): 
        while r < n_rows - 1 and not matrix[r][c]:
            r += 1
        return r
        
    def reduce_to_rref():
        for col in range(m_cols):
            pivot_row_idx = pivot_element(col)
            
            # Swap current row with found pivot element's row.
            if pivot_row_idx == n_rows:
                continue
                
            assert matrix[pivot_row_idx][col], "Matrix has no unique solution."
                
            # Make other elements zero below this one using subtraction.
            for row in range(pivot_row_idx + 1, n_rows):
                factor = int(matrix[row][col]) ^ int(matrix[pivot_row_idx][col])
                for idx_col in range(col, m_cols):
                    matrix[row][idx_col] ^= matrix[pivot_row_idx][idx_col]

    reduce_to_rref()
    
    num_non_zero_rows = sum([row[-1] for row in matrix])
    print(num_non_zero_rows)

N_M_input = input().split(' ')
n_equations, m_variables = map(int,N_M_input)
matrix = []
for _ in range(n_equations):
    row_input = input().strip().split(' ')[:-1]
    row_coeffs = ['' if char.isdigit() else '1' for char in row_input]
    row_coefficients = ''.join(row_coeffs)
    matrix.append(list(map(int,row_coefficients)))

gaussian_elimination(matrix)