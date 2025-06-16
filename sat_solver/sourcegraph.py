def parse_clauses(clauses_input):
    """
    Parse the input clauses into a list of lists.
    
    Args:
        clauses_input (list): List of strings representing clauses
        
    Returns:
        list: List of clauses, where each clause is a list of literals
    """
    clauses = []
    for line in clauses_input:
        literals = list(map(int, line.split()))
        # Remove the trailing 0
        clause = literals[:-1]
        clauses.append(clause)
    return clauses

def evaluate_clause(clause, assignment):
    """
    Evaluate a clause given an assignment.
    
    Args:
        clause (list): List of literals in the clause
        assignment (dict): Variable assignments {var: True/False}
        
    Returns:
        bool or None: True if satisfied, False if unsatisfied, None if undetermined
    """
    has_unassigned = False
    
    for literal in clause:
        var = abs(literal)
        positive = literal > 0
        
        if var in assignment:
            var_value = assignment[var]
            literal_value = var_value if positive else not var_value
            
            if literal_value:
                return True  # Clause is satisfied
        else:
            has_unassigned = True
    
    if has_unassigned:
        return None  # Clause is undetermined
    else:
        return False  # Clause is unsatisfied

def is_satisfiable(clauses, assignment):
    """
    Check if all clauses are satisfied by the current assignment.
    
    Args:
        clauses (list): List of clauses
        assignment (dict): Variable assignments
        
    Returns:
        bool or None: True if all satisfied, False if any unsatisfied, None if undetermined
    """
    all_satisfied = True
    
    for clause in clauses:
        result = evaluate_clause(clause, assignment)
        if result is False:
            return False  # Formula is unsatisfied
        elif result is None:
            all_satisfied = False  # Still undetermined
    
    return True if all_satisfied else None

def dpll(clauses, assignment, variables):
    """
    DPLL algorithm for SAT solving.
    
    Args:
        clauses (list): List of clauses
        assignment (dict): Current variable assignments
        variables (list): List of unassigned variables
        
    Returns:
        dict or None: Satisfying assignment if found, None if unsatisfiable
    """
    # Check current state
    result = is_satisfiable(clauses, assignment)
    
    if result is True:
        return assignment  # Found satisfying assignment
    elif result is False:
        return None  # Unsatisfiable
    
    # If no variables left to assign but formula not satisfied
    if not variables:
        return None
    
    # Choose next variable to assign
    var = variables[0]
    remaining_vars = variables[1:]
    
    # Try assigning True
    new_assignment = assignment.copy()
    new_assignment[var] = True
    
    result = dpll(clauses, new_assignment, remaining_vars)
    if result is not None:
        return result
    
    # Try assigning False
    new_assignment = assignment.copy()
    new_assignment[var] = False
    
    result = dpll(clauses, new_assignment, remaining_vars)
    return result

def solve_sat(n, clauses):
    """
    Solve the SAT problem.
    
    Args:
        n (int): Number of variables
        clauses (list): List of clauses
        
    Returns:
        tuple: (is_sat, assignment) where is_sat is bool and assignment is list
    """
    variables = list(range(1, n + 1))
    assignment = {}
    
    result = dpll(clauses, assignment, variables)
    
    if result is None:
        return False, None
    else:
        # Convert to output format
        output_assignment = []
        for i in range(1, n + 1):
            output_assignment.append(1 if result[i] else 0)
        return True, output_assignment

def main():
    # Read input
    n, m = map(int, input().split())
    
    clauses_input = []
    for _ in range(m):
        clauses_input.append(input().strip())
    
    # Parse clauses
    clauses = parse_clauses(clauses_input)
    
    # Solve SAT
    is_sat, assignment = solve_sat(n, clauses)
    
    # Output result
    if is_sat:
        print("SAT")
        print(" ".join(map(str, assignment)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()
