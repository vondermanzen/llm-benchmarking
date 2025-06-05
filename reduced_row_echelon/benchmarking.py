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

def generate_test_cases() -> List[Dict]:
    """Generate fixed test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example from prompt
    test_cases.append({
        "input": "3 3\n1 0 1 1\n0 1 1 0\n1 1 0 1",
        "output": "2",
        "description": "Example from prompt - rank 2 after elimination"
    })
    
    # Test case 2: Zero matrix
    test_cases.append({
        "input": "3 3\n0 0 0 0\n0 0 0 0\n0 0 0 0",
        "output": "0",
        "description": "Zero matrix - rank 0"
    })
    
    # Test case 3: Identity matrix
    test_cases.append({
        "input": "3 3\n1 0 0 1\n0 1 0 0\n0 0 1 1",
        "output": "3",
        "description": "Identity-like matrix - full rank"
    })
    
    # Test case 4: Dependent rows
    test_cases.append({
        "input": "4 3\n1 0 1 0\n0 1 1 1\n1 1 0 1\n1 1 0 1",
        "output": "2",
        "description": "Matrix with dependent rows - rank 2"
    })
    
    # Test case 5: Single row
    test_cases.append({
        "input": "1 4\n1 0 1 1",
        "output": "1",
        "description": "Single row matrix - rank 1"
    })
    
    # Test case 6: Larger matrix with rank 1
    test_cases.append({
        "input": "5 4\n1 0 1 0 1\n0 0 0 0 0\n1 0 1 0 1\n0 0 0 0 0\n1 0 1 0 1",
        "output": "1",
        "description": "5x4 matrix with multiple zero rows - rank 1"
    })
    
    # Test case 7: Inconsistent system
    test_cases.append({
        "input": "3 2\n1 0 1\n0 1 1\n1 1 0",
        "output": "2",
        "description": "3x2 system - rank 2"
    })
    
    return test_cases

# Current benchmarking script's filename
benchmark_file = 'benchmarking.py'

# List all .py files in the current directory except this one
py_files = [f for f in os.listdir('.') if f.endswith('.py') and f != benchmark_file]

results = {}
detailed_results = {}

# Generate test cases once to use for all solutions
test_cases = generate_test_cases()

for file in py_files:
    correct = 0
    total = len(test_cases)
    failed_cases = []
    
    for i, case in enumerate(test_cases):
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
            else:
                failed_cases.append({
                    'case_num': i + 1,
                    'description': case.get('description', f'Test case {i + 1}'),
                    'input': case["input"],
                    'expected': case["output"],
                    'actual': output,
                    'stderr': result.stderr.decode().strip() if result.stderr else None
                })
            
        except Exception as e:
            failed_cases.append({
                'case_num': i + 1,
                'description': case.get('description', f'Test case {i + 1}'),
                'input': case["input"],
                'expected': case["output"],
                'actual': 'ERROR',
                'error': str(e)
            })
    
    results[file] = f"{correct}/{total}"
    detailed_results[file] = failed_cases

# Print summary of results
print("\nScript Evaluation Results:")
print("-" * 30)
for script, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"{script}: {score}")

# Only show detailed failure analysis if not called from parent script
show_details = True
if len(sys.argv) > 1 and sys.argv[1] == "--no-details":
    show_details = False
elif os.path.basename(os.getcwd()) != os.path.basename(os.path.dirname(__file__)):
    # If current working directory is not the script's directory, likely called from parent
    show_details = False

if show_details:
    # Print detailed failure information
    print("\nDetailed Failure Analysis:")
    print("=" * 50)
    for script in sorted(py_files):
        score = results[script]
        if detailed_results[script]:
            print(f"\n{script} - {score} - Failed Cases:")
            print("-" * 30)
            for failure in detailed_results[script]:
                print(f"Test Case {failure['case_num']}: {failure['description']}")
                print(f"Input:\n{failure['input']}")
                print(f"Expected: {failure['expected']}")
                print(f"Actual: {failure['actual']}")
                if 'error' in failure:
                    print(f"Error: {failure['error']}")
                if failure.get('stderr'):
                    print(f"Stderr: {failure['stderr']}")
                print()
        else:
            print(f"\n{script}: {score}") 