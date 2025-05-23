import sys
import random
import numpy as np
from typing import List, Dict, Tuple

def matrix_to_str(matrix: List[List[int]]) -> str:
    """Convert a matrix to string format for input."""
    n = len(matrix)
    m = len(matrix[0]) - 1  # Last column is the constant term
    result = [f"{n} {m}"]
    for row in matrix:
        result.append(" ".join(map(str, row)))
    return "\n".join(result)

def generate_test_case(n: int, m: int, case_type: str = "random") -> Tuple[str, str]:
    """Generate a test case with n equations and m variables."""
    if case_type == "full_rank":
        # Generate a matrix that will definitely have full rank
        matrix = []
        for i in range(n):
            row = [0] * (m + 1)
            row[i] = 1
            if i < m:  # Add some random elements to make it interesting
                for j in range(i + 1, m):
                    row[j] = random.randint(0, 1)
            row[-1] = random.randint(0, 1)  # constant term
            matrix.append(row)
    
    elif case_type == "zero_rank":
        # Generate all-zero matrix
        matrix = [[0] * (m + 1) for _ in range(n)]
    
    elif case_type == "dependent":
        # Generate matrix with some dependent rows
        base_rows = min(n, m) // 2
        matrix = []
        # Generate independent rows
        for i in range(base_rows):
            row = [0] * (m + 1)
            row[i] = 1
            row[-1] = random.randint(0, 1)
            matrix.append(row)
        # Generate dependent rows
        while len(matrix) < n:
            new_row = [0] * (m + 1)
            # Combine 2-3 existing rows
            for _ in range(random.randint(2, 3)):
                if matrix:
                    row_idx = random.randint(0, len(matrix) - 1)
                    for j in range(m + 1):
                        new_row[j] = (new_row[j] + matrix[row_idx][j]) % 2
            matrix.append(new_row)
    
    else:  # random
        matrix = [[random.randint(0, 1) for _ in range(m + 1)] for _ in range(n)]
    
    return matrix_to_str(matrix)

def rref_mod2(matrix: List[List[int]]) -> List[List[int]]:
    """
    Compute the Reduced Row Echelon Form of matrix over GF(2).
    Returns the RREF matrix and its rank.
    """
    if not matrix or not matrix[0]:
        return [], 0
        
    n = len(matrix)
    m = len(matrix[0])
    
    # Convert to numpy array for easier manipulation
    A = np.array(matrix, dtype=int)
    
    # Keep track of where the pivots are
    pivot_cols = []
    row = 0
    
    for col in range(m):
        # Find pivot in this column
        pivot_row = None
        for r in range(row, n):
            if A[r, col] == 1:
                pivot_row = r
                break
        
        if pivot_row is not None:
            # Swap rows if necessary
            if pivot_row != row:
                A[row], A[pivot_row] = A[pivot_row].copy(), A[row].copy()
            
            # Eliminate above and below
            for r in range(n):
                if r != row and A[r, col] == 1:
                    A[r] = (A[r] + A[row]) % 2
            
            pivot_cols.append(col)
            row += 1
            
            if row == n:
                break
    
    # Convert back to list
    result = A.tolist()
    rank = len(pivot_cols)
    
    return result, rank

def verify_solution(test_input: str, expected_output: str, received_output: str) -> bool:
    """Verify if the received output matches the expected output."""
    try:
        # Parse input
        lines = test_input.strip().split("\n")
        n, m = map(int, lines[0].split())
        matrix = []
        for i in range(n):
            row = list(map(int, lines[i + 1].split()))
            matrix.append(row)
        
        # Compute correct rank
        _, correct_rank = rref_mod2(matrix)
        
        # Compare with received output
        received_rank = int(received_output.strip())
        return received_rank == correct_rank
        
    except:
        return False

def generate_test_cases() -> List[Dict]:
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example from prompt
    test_cases.append({
        "input": "3 3\n1 0 1 1\n0 1 1 0\n1 1 0 1",
        "output": "3"
    })
    
    # Test case 2: Small full rank matrix
    matrix = generate_test_case(3, 3, "full_rank")
    test_cases.append({
        "input": matrix,
        "output": None  # Will be computed
    })
    
    # Test case 3: Zero rank matrix
    matrix = generate_test_case(4, 4, "zero_rank")
    test_cases.append({
        "input": matrix,
        "output": None
    })
    
    # Test case 4: Matrix with dependent rows
    matrix = generate_test_case(5, 4, "dependent")
    test_cases.append({
        "input": matrix,
        "output": None
    })
    
    # Test case 5: Large random matrix
    matrix = generate_test_case(50, 40, "random")
    test_cases.append({
        "input": matrix,
        "output": None
    })
    
    # Compute expected outputs for generated test cases
    for case in test_cases:
        if case["output"] is None:
            lines = case["input"].strip().split("\n")
            n, m = map(int, lines[0].split())
            matrix = []
            for i in range(n):
                row = list(map(int, lines[i + 1].split()))
                matrix.append(row)
            _, rank = rref_mod2(matrix)
            case["output"] = str(rank)
    
    return test_cases

def run_tests(solution_file: str) -> None:
    """Run all test cases and score the solution."""
    try:
        with open(solution_file, 'r') as f:
            solution_code = f.read()
        
        # Create a temporary module to run the solution
        import importlib.util
        spec = importlib.util.spec_from_file_location("solution", solution_file)
        solution = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(solution)
        
        test_cases = generate_test_cases()
        total_score = 0
        max_score = len(test_cases)
        
        for i, case in enumerate(test_cases, 1):
            try:
                # Redirect stdin to provide input
                import io
                import sys
                sys.stdin = io.StringIO(case["input"])
                
                # Capture stdout
                from io import StringIO
                captured_output = StringIO()
                sys.stdout = captured_output
                
                # Run solution with timeout
                import threading
                import _thread
                def run_solution():
                    solution.main()
                
                thread = threading.Thread(target=run_solution)
                thread.start()
                thread.join(timeout=2)  # 2 second timeout
                
                if thread.is_alive():
                    _thread.interrupt_main()
                    raise TimeoutError("Solution took too long")
                
                received_output = captured_output.getvalue()
                
                # Verify output
                if verify_solution(case["input"], case["output"], received_output):
                    total_score += 1
                    print(f"Test case {i}: Passed")
                else:
                    print(f"Test case {i}: Failed")
                    print(f"Expected: {case['output']}")
                    print(f"Received: {received_output.strip()}")
                
            except Exception as e:
                print(f"Test case {i}: Error - {str(e)}")
            
            finally:
                # Reset stdin and stdout
                sys.stdin = sys.__stdin__
                sys.stdout = sys.__stdout__
        
        # Calculate and print final score
        final_score = (total_score / max_score) * 100
        print(f"\nFinal Score: {final_score:.2f}%")
        print(f"Passed {total_score} out of {max_score} test cases")
        
    except Exception as e:
        print(f"Error running tests: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python benchmarking.py <solution_file>")
        sys.exit(1)
    
    run_tests(sys.argv[1]) 