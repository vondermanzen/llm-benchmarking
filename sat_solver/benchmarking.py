import sys
import random
import subprocess
import os
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

def dpll(n: int, clauses: List[List[int]]) -> Tuple[bool, List[int]]:
    """Reference DPLL implementation."""
    def unit_propagate(clauses, assignment):
        """Find and apply unit clauses."""
        unit_found = True
        while unit_found:
            unit_found = False
            for clause in clauses:
                unassigned = []
                satisfied = False
                for lit in clause:
                    var = abs(lit)
                    if assignment[var - 1] == -1:
                        unassigned.append(lit)
                    elif (lit > 0 and assignment[var - 1] == 1) or \
                         (lit < 0 and assignment[var - 1] == 0):
                        satisfied = True
                        break
                if satisfied:
                    continue
                if len(unassigned) == 1:
                    unit_found = True
                    lit = unassigned[0]
                    var = abs(lit)
                    assignment[var - 1] = 1 if lit > 0 else 0
                    break
        return assignment

    def dpll_recursive(clauses, assignment):
        # Unit propagation
        assignment = unit_propagate(clauses, assignment)
        
        # Check if all clauses are satisfied
        all_satisfied = True
        for clause in clauses:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                if (lit > 0 and assignment[var - 1] == 1) or \
                   (lit < 0 and assignment[var - 1] == 0):
                    satisfied = True
                    break
            if not satisfied:
                all_satisfied = False
                break
        
        if all_satisfied:
            return True, assignment
            
        # Check if any clause is unsatisfied
        for clause in clauses:
            satisfied = False
            possible = False
            for lit in clause:
                var = abs(lit)
                if assignment[var - 1] == -1:
                    possible = True
                elif (lit > 0 and assignment[var - 1] == 1) or \
                     (lit < 0 and assignment[var - 1] == 0):
                    satisfied = True
                    break
            if not satisfied and not possible:
                return False, assignment
        
        # Choose a variable to branch on
        for i in range(n):
            if assignment[i] == -1:
                # Try assignment[i] = 1
                assignment[i] = 1
                result, new_assignment = dpll_recursive(clauses, assignment[:])
                if result:
                    return True, new_assignment
                    
                # Try assignment[i] = 0
                assignment[i] = 0
                result, new_assignment = dpll_recursive(clauses, assignment[:])
                if result:
                    return True, new_assignment
                    
                assignment[i] = -1
                return False, assignment
                
        return False, assignment

    assignment = [-1] * n  # -1 means unassigned
    return dpll_recursive(clauses, assignment)

def generate_test_case(case_type: str = "random") -> Tuple[str, str]:
    """Generate a test case based on the type."""
    if case_type == "always_sat":
        # Generate formula that's always satisfiable
        n = random.randint(3, 5)
        m = random.randint(3, 8)
        clauses = []
        for _ in range(m):
            var = random.randint(1, n)
            clauses.append([var])  # Unit clause, always satisfiable
        formula = f"{n} {m}\n" + "\n".join(" ".join(map(str, clause)) for clause in clauses)
        return formula, "SAT\n" + " ".join("1" for _ in range(n))
        
    elif case_type == "always_unsat":
        # Generate formula that's never satisfiable
        n = random.randint(2, 4)
        clauses = []
        # Add both x and not x for some variable
        var = random.randint(1, n)
        clauses.append([var])
        clauses.append([-var])
        formula = f"{n} 2\n" + "\n".join(" ".join(map(str, clause)) for clause in clauses)
        return formula, "UNSAT"
        
    elif case_type == "single_solution":
        # Generate formula with exactly one solution
        n = random.randint(3, 5)
        solution = [random.randint(0, 1) for _ in range(n)]
        clauses = []
        # Add clauses that force this solution
        for i in range(n):
            clauses.append([i + 1 if solution[i] else -(i + 1)])
        formula = f"{n} {len(clauses)}\n" + "\n".join(" ".join(map(str, clause)) for clause in clauses)
        return formula, "SAT\n" + " ".join(map(str, solution))
        
    else:  # random
        n = random.randint(3, 5)
        m = random.randint(3, 8)
        clauses = []
        for _ in range(m):
            clause_size = random.randint(1, 3)
            clause = []
            for _ in range(clause_size):
                var = random.randint(1, n)
                sign = random.choice([-1, 1])
                clause.append(sign * var)
            clauses.append(clause)
        
        # Solve with DPLL to determine if satisfiable
        is_sat, assignment = dpll(n, clauses)
        formula = f"{n} {m}\n" + "\n".join(" ".join(map(str, clause)) for clause in clauses)
        if is_sat:
            return formula, "SAT\n" + " ".join(map(str, assignment))
        else:
            return formula, "UNSAT"

def generate_test_cases() -> List[Dict]:
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example case
    test_cases.append({
        "input": "1\n2 2\n1 2\n-1 -2",
        "output": "SAT\n0 0"
    })
    
    # Test case 2: Multiple test cases with different types
    cases = [
        generate_test_case("always_sat"),
        generate_test_case("always_unsat"),
        generate_test_case("single_solution"),
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
            
            # Special handling for SAT problems
            # If the output is SAT, verify the solution
            lines = output.split("\n")
            expected_lines = case["output"].split("\n")
            if len(lines) > 0 and len(expected_lines) > 0:
                if expected_lines[0] == "UNSAT":
                    if lines[0] == "UNSAT":
                        correct += 1
                elif expected_lines[0] == "SAT" and lines[0] == "SAT":
                    # Parse the input to get n and clauses
                    input_lines = case["input"].split("\n")
                    if input_lines[0] == "1":  # Single test case
                        n, m = map(int, input_lines[1].split())
                        clauses = []
                        for i in range(m):
                            clause = list(map(int, input_lines[i + 2].split()))
                            clauses.append(clause)
                        # Parse the solution
                        if len(lines) > 1:
                            try:
                                solution = list(map(int, lines[1].split()))
                                if verify_sat_solution(n, clauses, solution):
                                    correct += 1
                            except:
                                pass
            
        except Exception as e:
            pass  # Failed test case
    
    results[file] = f"{correct}/{total}"

# Print summary of results
print("\nScript Evaluation Results:")
print("-" * 30)
for script, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"{script}: {score}") 