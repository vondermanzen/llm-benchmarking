#!/usr/bin/env python3
"""
Matrix Rank over GF(2) Calculator

This program computes the rank of a matrix over GF(2) (binary field) using
Gaussian elimination with modulo 2 arithmetic. All operations are performed
in the Galois Field with 2 elements where addition is XOR and multiplication
is AND.

Author: Matrix Rank Calculator
Date: June 20, 2025
"""

import sys
from typing import List, Tuple


def read_input() -> Tuple[int, int, List[List[int]]]:
    """
    Read input from stdin and parse the matrix.
    
    Returns:
        Tuple containing:
        - N: number of equations
        - M: number of variables  
        - matrix: augmented matrix [A|b] as list of lists
    """
    try:
        # Read dimensions
        line = input().strip()
        N, M = map(int, line.split())
        
        if N <= 0 or M <= 0 or N > 1000 or M > 1000:
            raise ValueError(f"Invalid dimensions: N={N}, M={M}. Must be between 1 and 1000.")
        
        # Read matrix rows
        matrix = []
        for i in range(N):
            line = input().strip()
            row = list(map(int, line.split()))
            
            if len(row) != M + 1:
                raise ValueError(f"Row {i+1} has {len(row)} elements, expected {M+1}")
            
            # Validate binary values
            for j, val in enumerate(row):
                if val not in [0, 1]:
                    raise ValueError(f"Invalid value {val} at row {i+1}, column {j+1}. Only 0 and 1 are allowed.")
            
            matrix.append(row)
        
        return N, M, matrix
    
    except EOFError:
        print("Error: Unexpected end of input", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)


def print_matrix(matrix: List[List[int]], title: str = "") -> None:
    """
    Debug function to print matrix (not used in final output).
    
    Args:
        matrix: The matrix to print
        title: Optional title for the matrix
    """
    if title:
        print(f"\n{title}:", file=sys.stderr)
    for row in matrix:
        print(" ".join(map(str, row)), file=sys.stderr)


def gaussian_elimination_gf2(matrix: List[List[int]]) -> int:
    """
    Perform Gaussian elimination over GF(2) to find the rank.
    
    In GF(2):
    - Addition is XOR (a + b = a ⊕ b)
    - Multiplication is AND (a * b = a ∧ b)
    - Subtraction is the same as addition (since -1 = 1 in GF(2))
    
    Args:
        matrix: Augmented matrix [A|b] where each row represents an equation
    
    Returns:
        The rank of the matrix (number of non-zero rows after reduction)
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a copy to avoid modifying the original
    mat = [row[:] for row in matrix]
    
    current_row = 0
    
    # Process each column (except we go through all columns including the augmented column)
    for col in range(cols):
        # Find pivot in current column starting from current_row
        pivot_row = -1
        for row in range(current_row, rows):
            if mat[row][col] == 1:
                pivot_row = row
                break
        
        # If no pivot found in this column, continue to next column
        if pivot_row == -1:
            continue
        
        # Swap current row with pivot row if needed
        if pivot_row != current_row:
            mat[current_row], mat[pivot_row] = mat[pivot_row], mat[current_row]
        
        # Eliminate all other 1's in this column using XOR operations
        for row in range(rows):
            if row != current_row and mat[row][col] == 1:
                # Add current_row to row (XOR operation in GF(2))
                for c in range(cols):
                    mat[row][c] ^= mat[current_row][c]
        
        current_row += 1
        
        # If we've processed all rows, we're done
        if current_row >= rows:
            break
    
    # Count non-zero rows to determine rank
    rank = 0
    for row in range(rows):
        # Check if row has any non-zero elements
        if any(mat[row][col] == 1 for col in range(cols)):
            rank += 1
    
    return rank


def is_zero_row(row: List[int]) -> bool:
    """
    Check if a row contains only zeros.
    
    Args:
        row: A row from the matrix
    
    Returns:
        True if the row is all zeros, False otherwise
    """
    return all(val == 0 for val in row)


def main():
    """
    Main function to execute the matrix rank calculation.
    """
    try:
        # Read input
        N, M, matrix = read_input()
        
        # Compute rank using Gaussian elimination over GF(2)
        rank = gaussian_elimination_gf2(matrix)
        
        # Output the result
        print(rank)
    
    except KeyboardInterrupt:
        print("\nProgram interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
