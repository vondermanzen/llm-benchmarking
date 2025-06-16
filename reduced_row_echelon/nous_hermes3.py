def matrix_rank_over_gf2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rank = 0
    
    for col in range(cols):
        if col >= rows:
            break
        
        row = col
        while row < rows and matrix[row][col] == 0:
            row += 1
        
        if row == rows:
            continue
        
        if row != col:
            matrix[col], matrix[row] = matrix[row], matrix[col]
        
        for row2 in range(row + 1, rows):
            if matrix[row2][col] == 1:
                for col2 in range(col, cols):
                    matrix[row2][col2] ^= matrix[col][col2]
        
        rank += 1
    
    return rank

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    rank = matrix_rank_over_gf2(matrix)
    print(rank)

if __name__ == "__main__":
    main()