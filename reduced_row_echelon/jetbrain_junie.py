#!/usr/bin/env python3

def read_input():
    """
    Read the input in the specified format.

    Returns:
        tuple: (matrix, n, m) where matrix is the augmented matrix,
               n is the number of equations, and m is the number of variables
    """
    n, m = map(int, input().strip().split())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().strip().split()))
        matrix.append(row)

    return matrix, n, m

def gaussian_elimination_gf2(matrix, n, m):
    """
    Perform Gaussian elimination over GF(2) to convert the matrix to reduced row echelon form.

    Args:
        matrix: The augmented matrix [A|b]
        n: Number of equations
        m: Number of variables

    Returns:
        list: The matrix in reduced row echelon form
    """
    # Make a copy of the matrix to avoid modifying the original
    rref = [row[:] for row in matrix]

    # Number of columns in the augmented matrix
    cols = m + 1

    # Forward elimination
    lead = 0
    for r in range(n):
        if lead >= cols:
            break

        # Find the pivot row
        i = r
        while i < n and rref[i][lead] == 0:
            i += 1

        if i == n:  # No pivot in this column, move to next column
            lead += 1
            if lead < cols:
                r -= 1  # Process this row again with next column
            continue

        # Swap rows
        rref[r], rref[i] = rref[i], rref[r]

        # Eliminate below
        for i in range(n):
            if i != r and rref[i][lead] == 1:
                for j in range(lead, cols):
                    rref[i][j] = (rref[i][j] + rref[r][j]) % 2

        lead += 1

    # Back-substitution to get reduced row echelon form
    for r in range(n-1, -1, -1):
        # Find the leading 1 in this row
        lead = -1
        for j in range(cols-1):
            if rref[r][j] == 1:
                lead = j
                break

        if lead != -1:
            # Eliminate above
            for i in range(r):
                if rref[i][lead] == 1:
                    for j in range(lead, cols):
                        rref[i][j] = (rref[i][j] + rref[r][j]) % 2

    return rref

def calculate_rank(matrix):
    """
    Calculate the rank of a matrix in reduced row echelon form.

    Args:
        matrix: The matrix in reduced row echelon form

    Returns:
        int: The rank of the matrix
    """
    rank = 0
    for row in matrix:
        if any(row):  # Check if the row contains any non-zero element
            rank += 1
    return rank

def main():
    # Read input
    matrix, n, m = read_input()

    # Perform Gaussian elimination
    rref = gaussian_elimination_gf2(matrix, n, m)

    # Calculate and print the rank
    rank = calculate_rank(rref)
    print(rank)

if __name__ == '__main__':
    main()

