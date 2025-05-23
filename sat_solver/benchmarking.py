import sys
import random
from typing import List, Dict, Set, Optional, Tuple

def evaluate_assignment(clauses: List[List[int]], assignment: List[int]) -> bool:
    """Evaluate if an assignment satisfies all clauses."""
    for clause in clauses:
        clause_satisfied = False
        for literal in clause:
            if literal > 0:
                if assignment[literal - 1] == 1:
                    clause_satisfied = True
                    break
            else:
                if assignment[-literal - 1] == 0:
                    clause_satisfied = True
                    break
        if not clause_satisfied:
            return False
    return True

def solve_sat(n: int, clauses: List[List[int]]) -> Optional[List[int]]:
    """
    Solve SAT using DPLL algorithm.
    This is the reference solution used to verify if a formula is satisfiable.
    """
    def unit_propagate(clauses: List[List[int]], assignment: List[Optional[int]]) -> bool:
        """Perform unit propagation."""
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned = []
                clause_sat = False
                for lit in clause:
                    var = abs(lit) - 1
                    if assignment[var] is None:
                        unassigned.append(lit)
                    elif (lit > 0 and assignment[var] == 1) or (lit < 0 and assignment[var] == 0):
                        clause_sat = True
                        break
                
                if clause_sat:
                    continue
                
                if len(unassigned) == 0:
                    return False
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit) - 1
                    val = 1 if lit > 0 else 0
                    assignment[var] = val
                    changed = True
        return True

    def dpll(clauses: List[List[int]], assignment: List[Optional[int]]) -> bool:
        """DPLL recursive algorithm."""
        if not unit_propagate(clauses, assignment):
            return False
        
        # Check if all variables are assigned
        if all(v is not None for v in assignment):
            return True
        
        # Choose unassigned variable
        var = assignment.index(None)
        
        # Try both values
        for val in [0, 1]:
            assignment[var] = val
            if dpll(clauses, assignment[:]):
                return True
        
        assignment[var] = None
        return False

    assignment = [None] * n
    if dpll(clauses, assignment):
        return assignment
    return None

def format_cnf(n: int, clauses: List[List[int]]) -> str:
    """Convert clauses to input string format."""
    result = [f"{n} {len(clauses)}"]
    for clause in clauses:
        result.append(" ".join(map(str, clause + [0])))
    return "\n".join(result)

def generate_test_case(n: int, m: int, case_type: str = "random") -> str:
    """Generate a test case with n variables and m clauses."""
    clauses = []
    
    if case_type == "satisfiable":
        # Generate a formula that we know is satisfiable
        solution = [random.randint(0, 1) for _ in range(n)]
        
        # Generate clauses that are satisfied by our solution
        for _ in range(m):
            clause = []
            # Add 1-3 literals that make the clause true
            for _ in range(random.randint(1, 3)):
                var = random.randint(1, n)
                if solution[var - 1] == 1:
                    clause.append(var)
                else:
                    clause.append(-var)
            clauses.append(clause)
            
    elif case_type == "unsatisfiable":
        # Generate a simple unsatisfiable formula
        # (x₁ ∧ ¬x₁) ∧ (easy clauses...)
        clauses = [[1], [-1]]
        # Add some random satisfiable clauses
        while len(clauses) < m:
            clause = []
            for _ in range(random.randint(1, 3)):
                var = random.randint(2, n)
                clause.append(var if random.random() > 0.5 else -var)
            clauses.append(clause)
            
    else:  # random
        # Generate random clauses
        for _ in range(m):
            clause = []
            clause_size = random.randint(1, 3)
            used_vars = set()
            
            while len(clause) < clause_size:
                var = random.randint(1, n)
                if var not in used_vars:
                    used_vars.add(var)
                    clause.append(var if random.random() > 0.5 else -var)
            clauses.append(clause)
    
    return format_cnf(n, clauses)

def parse_output(output: str, n: int) -> Optional[List[int]]:
    """Parse and validate the solution output."""
    try:
        lines = output.strip().split("\n")
        if lines[0] == "UNSAT":
            return None
        if lines[0] != "SAT" or len(lines) != 2:
            return "INVALID"
            
        assignment = list(map(int, lines[1].split()))
        if len(assignment) != n or not all(x in [0, 1] for x in assignment):
            return "INVALID"
            
        return assignment
    except:
        return "INVALID"

def verify_solution(test_input: str, expected_output: str, received_output: str) -> bool:
    """Verify if the received output matches the expected output."""
    try:
        # Parse input
        lines = test_input.strip().split("\n")
        n, m = map(int, lines[0].split())
        clauses = []
        for i in range(m):
            nums = list(map(int, lines[i + 1].split()))
            clauses.append(nums[:-1])  # Remove the trailing 0
        
        # Parse output
        received_assignment = parse_output(received_output, n)
        if received_assignment == "INVALID":
            return False
            
        # If solution says UNSAT
        if received_assignment is None:
            # Verify using our solver that it really is UNSAT
            reference_solution = solve_sat(n, clauses)
            return reference_solution is None
            
        # Verify the assignment satisfies all clauses
        return evaluate_assignment(clauses, received_assignment)
        
    except:
        return False

def generate_test_cases() -> List[Dict]:
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example from prompt
    test_cases.append({
        "input": "3 2\n1 2 0\n-1 -2 3 0",
        "output": None  # Will be computed
    })
    
    # Test case 2: Small unsatisfiable formula
    test_cases.append({
        "input": "2 3\n1 0\n-1 0\n2 -2 0",
        "output": None
    })
    
    # Test case 3: Known satisfiable formula
    test_cases.append({
        "input": generate_test_case(5, 8, "satisfiable"),
        "output": None
    })
    
    # Test case 4: Another unsatisfiable formula
    test_cases.append({
        "input": generate_test_case(4, 6, "unsatisfiable"),
        "output": None
    })
    
    # Test case 5: Large random formula
    test_cases.append({
        "input": generate_test_case(15, 40, "random"),
        "output": None
    })
    
    # Compute expected outputs for all test cases
    for case in test_cases:
        lines = case["input"].strip().split("\n")
        n, m = map(int, lines[0].split())
        clauses = []
        for i in range(m):
            nums = list(map(int, lines[i + 1].split()))
            clauses.append(nums[:-1])
        
        solution = solve_sat(n, clauses)
        if solution is None:
            case["output"] = "UNSAT\n"
        else:
            case["output"] = "SAT\n" + " ".join(map(str, solution))
    
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
                    print(f"Input:")
                    print(case["input"])
                    print(f"Expected type: {'UNSAT' if 'UNSAT' in case['output'] else 'SAT'}")
                    print(f"Received output:")
                    print(received_output.strip())
                
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