import sys
import random
import numpy as np
import subprocess
import os
from typing import List, Dict, Tuple

def matrix_to_str(matrix: List[List[int]]) -> str:
    """Convert a matrix to string format for input."""
    n = len(matrix)
    m = len(matrix[0]) - 1  # Last column is the constant term
    result = [f"{n} {m}"]
    for row in matrix:
        result.append(" ".join(map(str, row)))
    return "\n".join(result)

def calculate_rank_gf2(matrix: List[List[int]]) -> int:
    """Calculate the rank of a matrix over GF(2)."""
    if not matrix or not matrix[0]:
        return 0
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Make a copy to not modify the input
    mat = [row[:] for row in matrix]
    rank = 0
    
    # For each column
    for col in range(cols):
        # Find a row with 1 in current column
        pivot_row = None
        for row in range(rank, rows):
            if mat[row][col] == 1:
                pivot_row = row
                break
                
        if pivot_row is not None:
            # Swap with current row if needed
            if pivot_row != rank:
                mat[rank], mat[pivot_row] = mat[pivot_row], mat[rank]
            
            # Eliminate this column from other rows
            for row in range(rows):
                if row != rank and mat[row][col] == 1:
                    # XOR operation in GF(2)
                    for c in range(col, cols):
                        mat[row][c] ^= mat[rank][c]
            
            rank += 1
    
    return rank

def generate_test_case(case_type: str = "random") -> Tuple[str, str]:
    """Generate a test case based on the type."""
    if case_type == "full_rank":
        # Generate matrix with full rank
        n = random.randint(3, 6)
        matrix = []
        # Start with identity matrix
        for i in range(n):
            row = [0] * n
            row[i] = 1
            matrix.append(row)
        # Add some random operations to mix it up
        for _ in range(n):
            r1, r2 = random.sample(range(n), 2)
            for j in range(n):
                matrix[r1][j] ^= matrix[r2][j]
        return (
            f"{n} {n}\n" + "\n".join(" ".join(map(str, row)) for row in matrix),
            str(n)
        )
        
    elif case_type == "zero_rank":
        # Generate zero matrix
        n = random.randint(3, 6)
        m = random.randint(3, 6)
        matrix = [[0] * m for _ in range(n)]
        return (
            f"{n} {m}\n" + "\n".join(" ".join(map(str, row)) for row in matrix),
            "0"
        )
        
    elif case_type == "dependent_rows":
        # Generate matrix with some dependent rows
        n = random.randint(4, 6)
        m = random.randint(4, 6)
        rank = random.randint(2, min(n-1, m-1))
        matrix = []
        # Generate independent rows
        for i in range(rank):
            row = [random.randint(0, 1) for _ in range(m)]
            while all(x == 0 for x in row):  # Ensure non-zero row
                row = [random.randint(0, 1) for _ in range(m)]
            matrix.append(row)
        # Generate dependent rows
        for i in range(n - rank):
            # Take random combination of existing rows
            row = [0] * m
            for j in range(rank):
                if random.random() < 0.5:
                    for k in range(m):
                        row[k] ^= matrix[j][k]
            if all(x == 0 for x in row):  # If got zero row, use first row
                row = matrix[0][:]
            matrix.append(row)
        # Shuffle rows
        random.shuffle(matrix)
        return (
            f"{n} {m}\n" + "\n".join(" ".join(map(str, row)) for row in matrix),
            str(rank)
        )
        
    else:  # random
        n = random.randint(3, 6)
        m = random.randint(3, 6)
        matrix = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]
        return (
            f"{n} {m}\n" + "\n".join(" ".join(map(str, row)) for row in matrix),
            str(calculate_rank_gf2(matrix))
        )

def generate_test_cases() -> List[Dict]:
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example case
    test_cases.append({
        "input": "1\n3 3\n1 0 0\n0 1 0\n0 0 1",
        "output": "3"
    })
    
    # Test case 2: Multiple test cases with different types
    cases = [
        generate_test_case("full_rank"),
        generate_test_case("zero_rank"),
        generate_test_case("dependent_rows"),
        generate_test_case("random")
    ]
    combined_input = str(len(cases)) + "\n" + "\n".join(input_str for input_str, _ in cases)
    combined_output = "\n".join(output for _, output in cases)
    test_cases.append({
        "input": combined_input,
        "output": combined_output
    })
    
    # Test case 3: Large random cases
    random_cases = [generate_test_case("random") for _ in range(5)]
    combined_input = str(len(random_cases)) + "\n" + "\n".join(input_str for input_str, _ in random_cases)
    combined_output = "\n".join(output for _, output in random_cases)
    test_cases.append({
        "input": combined_input,
        "output": combined_output
    })
    
    return test_cases

# Current benchmarking script's filename
benchmark_file = 'benchmarking.py'

# List all .py files in the current directory except this one
py_files = [f for f in os.listdir('.') if f.endswith('.py') and f != benchmark_file]

results = {}

# Generate test cases once to use for all solutions
test_cases = generate_test_cases()

for file in py_files:
    correct = 0
    total = len(test_cases)
    
    for case in test_cases:
        try:
            # Run the script with input and capture output
            result = subprocess.run(
                ['python', file],
                input=case["input"].encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=2  # 2 second timeout per test case
            )
            output = result.stdout.decode().strip()
            if output == case["output"]:
                correct += 1
            
        except Exception as e:
            pass  # Failed test case
    
    results[file] = f"{correct}/{total}"

# Print summary of results
print("\nScript Evaluation Results:")
print("-" * 30)
for script, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"{script}: {score}") 