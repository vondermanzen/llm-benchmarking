def compute_rank_gf2(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rank = 0
    
    for col in range(m):
        # Find pivot row
        for row in range(rank, n):
            if matrix[row][col] == 1:
                # Swap rows
                matrix[rank], matrix[row] = matrix[row], matrix[rank]
                break
        else:
            # No pivot found in this column
            continue
        
        # Eliminate other rows
        for row in range(n):
            if row != rank and matrix[row][col] == 1:
                # XOR operation (addition in GF(2))
                for c in range(col, m):
                    matrix[row][c] = (matrix[row][c] ^ matrix[rank][c])
        
        rank += 1
        if rank == n:
            break
    
    return rank

def main():
    n, m = map(int, input().split())
    matrix = []
    
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    rank = compute_rank_gf2(matrix)
    print(rank)

if __name__ == "__main__":
    main()