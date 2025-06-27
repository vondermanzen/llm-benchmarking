def gauss_elimination_gf2(matrix):
    """
    Perform Gaussian elimination over GF(2) to find the rank.

    Args:
        matrix: List of lists representing the augmented matrix

    Returns:
        int: The rank of the matrix (number of non-zero rows)
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # Create a copy to avoid modifying the original
    mat = [row[:] for row in matrix]

    current_row = 0

    # Forward elimination
    for col in range(cols):
        # Find pivot row (first row with 1 in current column)
        pivot_row = None
        for row in range(current_row, rows):
            if mat[row][col] == 1:
                pivot_row = row
                break

        # If no pivot found, move to next column
        if pivot_row is None:
            continue

        # Swap current row with pivot row if needed
        if pivot_row != current_row:
            mat[current_row], mat[pivot_row] = mat[pivot_row], mat[current_row]

        # Eliminate all other 1s in this column (both above and below)
        for row in range(rows):
            if row != current_row and mat[row][col] == 1:
                # XOR the rows (addition in GF(2))
                for c in range(cols):
                    mat[row][c] ^= mat[current_row][c]

        current_row += 1

        # If we've processed all rows, we're done
        if current_row >= rows:
            break

    # Count non-zero rows
    rank = 0
    for row in mat:
        if any(val == 1 for val in row):
            rank += 1

    return rank


def main():
    # Read input
    n, m = map(int, input().split())

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Calculate rank over GF(2)
    rank = gauss_elimination_gf2(matrix)

    # Output result
    print(rank)


if __name__ == "__main__":
    main()

