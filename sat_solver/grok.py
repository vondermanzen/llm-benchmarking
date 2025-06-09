def evaluate_clause(clause, assignment):
    """Evaluate if a clause is satisfied under given assignment."""
    for literal in clause:
        if literal == 0:  # End of clause
            break
        var = abs(literal)
        is_negated = literal < 0
        var_value = assignment[var - 1]
        # If literal is positive and var is True, or literal is negative and var is False
        if (not is_negated and var_value) or (is_negated and not var_value):
            return True
    return False

def is_satisfiable(clauses, assignment, n):
    """Check if all clauses are satisfied with current assignment."""
    return all(evaluate_clause(clause, assignment) for clause in clauses)

def solve_sat(clauses, n, assignment, var_idx):
    """Recursively try assignments to find a satisfying one."""
    if var_idx == n:  # All variables assigned
        return is_satisfiable(clauses, assignment, n)
    
    # Try assigning False (0)
    assignment[var_idx] = 0
    if solve_sat(clauses, n, assignment, var_idx + 1):
        return True
    
    # Try assigning True (1)
    assignment[var_idx] = 1
    if solve_sat(clauses, n, assignment, var_idx + 1):
        return True
    
    return False

def main():
    # Read input
    n, m = map(int, input().split())
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clauses.append(clause)
    
    # Initialize assignment array
    assignment = [0] * n
    
    # Solve SAT problem
    if solve_sat(clauses, n, assignment, 0):
        print("SAT")
        print(" ".join(map(str, assignment)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()