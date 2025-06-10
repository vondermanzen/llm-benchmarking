import sys
import subprocess
import os
import time
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

def verify_sat_solution(n: int, clauses: List[List[int]], assignment: List[int]) -> bool:
    """Verify if the assignment satisfies all clauses."""
    if len(assignment) != n:
        return False
        
    # Check each clause
    for clause in clauses:
        satisfied = False
        for literal in clause:
            var = abs(literal)
            val = assignment[var - 1]
            if (literal > 0 and val == 1) or (literal < 0 and val == 0):
                satisfied = True
                break
        if not satisfied:
            return False
    return True

def generate_test_cases() -> List[Dict]:
    """Generate hardcoded test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Simple satisfiable case
    test_cases.append({
        "input": "2 2\n1 2 0\n-1 -2 0",
        "output": "SAT\n0 0",
        "description": "Simple SAT - (x1∨x2)∧(¬x1∨¬x2) accepts any valid assignment"
    })
    
    # Test case 2: Simple unsatisfiable case
    test_cases.append({
        "input": "1 2\n1 0\n-1 0",
        "output": "UNSAT",
        "description": "Simple UNSAT - contradictory unit clauses x1 and ¬x1"
    })
    
    # Test case 3: Single variable satisfiable
    test_cases.append({
        "input": "1 1\n1 0",
        "output": "SAT\n1",
        "description": "Single variable SAT - x1 must be true (only one valid assignment)"
    })
    
    # Test case 4: Three variables, satisfiable
    test_cases.append({
        "input": "3 3\n1 2 3 0\n-1 2 0\n-2 3 0",
        "output": "SAT\n0 1 1",
        "description": "3-SAT satisfiable - (x1∨x2∨x3)∧(¬x1∨x2)∧(¬x2∨x3) has valid assignments"
    })
    
    # Test case 5: Horn clauses, unsatisfiable  
    test_cases.append({
        "input": "3 4\n1 0\n-1 2 0\n-2 3 0\n-3 0",
        "output": "UNSAT",
        "description": "Horn clauses UNSAT - unit propagation leads to contradiction"
    })
    
    # Test case 6: Unsatisfiable 3-SAT
    test_cases.append({
        "input": "2 4\n1 2 0\n1 -2 0\n-1 2 0\n-1 -2 0",
        "output": "UNSAT",
        "description": "UNSAT 3-SAT - all possible assignments of x1,x2 lead to contradiction"
    })
    
    # Test case 7: Example from prompt
    test_cases.append({
        "input": "3 2\n1 2 0\n-1 -2 3 0",
        "output": "SAT\n0 0 1",
        "description": "Example from prompt - (x1∨x2)∧(¬x1∨¬x2∨x3) has multiple valid assignments"
    })
    
    # Test case 8: Larger satisfiable case
    test_cases.append({
        "input": "4 5\n1 2 0\n-1 3 0\n-2 4 0\n-3 -4 0\n1 4 0",
        "output": "SAT\n1 1 1 0",
        "description": "4-variable SAT with implication chain - multiple valid assignments"
    })
    
    # Test case 9: Empty clause (immediately UNSAT)
    test_cases.append({
        "input": "2 3\n1 2 0\n0\n-1 -2 0",
        "output": "UNSAT",
        "description": "Empty clause makes formula immediately UNSAT"
    })
    
    # Test case 10: Tautology clauses (should be SAT)
    test_cases.append({
        "input": "2 2\n1 -1 0\n2 -2 0",
        "output": "SAT\n0 0",
        "description": "Tautology clauses - always satisfiable with any assignment"
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
    total_time = 0
    
    for i, case in enumerate(test_cases):
        try:
            # Run the script with input and capture output
            start_time = time.time()
            result = subprocess.run(
                ['python', file],
                input=case["input"].encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=2  # 2 second timeout per test case
            )
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            output = result.stdout.decode().strip()
            
            # Parse the single test case
            input_lines = case["input"].split("\n")
            n, m = map(int, input_lines[0].split())
            
            clauses = []
            for clause_idx in range(1, m + 1):
                if clause_idx < len(input_lines):
                    clause = list(map(int, input_lines[clause_idx].split()[:-1]))  # Remove trailing 0
                    clauses.append(clause)
            
            # Check the output
            expected_outputs = case["output"].split("\n")
            actual_outputs = output.split("\n") if output else []
            
            test_passed = True
            failure_reason = ""
            
            if len(actual_outputs) < len(expected_outputs):
                test_passed = False
                failure_reason = f"Expected {len(expected_outputs)} output lines, got {len(actual_outputs)}"
            else:
                expected_result = expected_outputs[0]
                actual_result = actual_outputs[0] if actual_outputs else ""
                
                if expected_outputs[0] == "UNSAT":
                    if actual_result != "UNSAT":
                        test_passed = False
                        failure_reason = f"Expected UNSAT, got '{actual_result}'"
                elif expected_outputs[0] == "SAT":
                    if actual_result.strip() != "SAT":
                        test_passed = False
                        failure_reason = f"Expected SAT, got '{actual_result}'"
                    else:
                        # Verify the assignment - accept ANY valid assignment
                        if len(actual_outputs) < 2:
                            test_passed = False
                            failure_reason = "Missing assignment for SAT"
                        else:
                            try:
                                assignment = list(map(int, actual_outputs[1].split()))
                                if len(assignment) != n:
                                    test_passed = False
                                    failure_reason = f"Assignment length {len(assignment)} != {n} variables"
                                elif not verify_sat_solution(n, clauses, assignment):
                                    test_passed = False
                                    failure_reason = f"Invalid assignment {assignment} - doesn't satisfy all clauses"
                                else:
                                    # Assignment is valid! Accept it regardless of what our expected output was
                                    test_passed = True
                                    failure_reason = ""  # Clear any previous failure reason
                            except (ValueError, IndexError) as e:
                                test_passed = False
                                failure_reason = f"Malformed assignment: {e}"
                else:
                    test_passed = False
                    failure_reason = f"Unexpected expected result: {expected_outputs[0]}"
            
            if test_passed:
                correct += 1
                total_time += execution_time
            else:
                failed_cases.append({
                    'case_num': i + 1,
                    'description': case.get('description', f'Test case {i + 1}'),
                    'input': case["input"],
                    'expected': case["output"],
                    'actual': output,
                    'failure_reason': failure_reason,
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
    
    # Calculate average time for correct solutions
    avg_time = total_time / correct if correct > 0 else float('inf')
    results[file] = {
        'score': f"{correct}/{total}",
        'avg_time_ms': round(avg_time, 2)
    }
    detailed_results[file] = failed_cases

# Print summary of results
print("Script Evaluation Results:")
print("-" * 50)
print(f"{'Script':<20} {'Score':<10} {'Avg Time (ms)':<15}")
print("-" * 50)
for script, result in sorted(results.items(), key=lambda x: (x[1]['score'], -x[1]['avg_time_ms']), reverse=True):
    print(f"{script:<20} {result['score']:<10} {result['avg_time_ms']:<15.2f}")

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
        score = results[script]['score']
        if detailed_results[script]:
            print(f"\n{script} - {score} - Failed Cases:")
            print("-" * 30)
            for failure in detailed_results[script]:
                print(f"Test Case {failure['case_num']}: {failure['description']}")
                print(f"Input:\n{failure['input']}")
                print(f"Expected: {failure['expected']}")
                print(f"Actual: {failure['actual']}")
                if 'failure_reason' in failure:
                    print(f"Reason: {failure['failure_reason']}")
                if 'error' in failure:
                    print(f"Error: {failure['error']}")
                if failure.get('stderr'):
                    print(f"Stderr: {failure['stderr']}")
                print()
        else:
            print(f"\n{script}: {score}") 