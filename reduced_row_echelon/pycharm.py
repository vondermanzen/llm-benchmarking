def compute_matrix_rank_gf2(matrix):
    """
    Compute the rank of a matrix over GF(2) (binary field).
    All operations are performed modulo 2.

    Args:
        matrix: A 2D list representing the matrix.

    Returns:
        int: The rank of the matrix.
    """
    # Make a copy of the matrix to avoid modifying the original
    m = [row[:] for row in matrix]
    rows, cols = len(m), len(m[0])

    # Gaussian elimination over GF(2)
    rank = 0
    for c in range(cols):
        # Find pivot row
        for r in range(rank, rows):
            if m[r][c] == 1:
                # Swap rows
                m[rank], m[r] = m[r], m[rank]
                break
        else:
            # No pivot in this column, continue to next column
            continue

        # Eliminate below
        for r in range(rank + 1, rows):
            if m[r][c] == 1:
                # XOR operation (addition in GF(2))
                for j in range(c, cols):
                    m[r][j] = (m[r][j] ^ m[rank][j])

        rank += 1

        # If we've processed all rows, we're done
        if rank == rows:
            break

    # Count non-zero rows
    return rank

def main():
    # Read input
    n, m = map(int, input().split())

    # Read the augmented matrix [A|b]
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Compute the rank
    rank = compute_matrix_rank_gf2(matrix)

    # Print the result
    print(rank)

if __name__ == "__main__":
    main()