def dpll(formula, assignment, variables):
    """
    DPLL algorithm for solving SAT problems.
    
    Args:
        formula (list): List of clauses, where each clause is a list of literals
        assignment (dict): Current variable assignments (variable -> True/False)
        variables (list): List of variables to assign
        
    Returns:
        dict or None: A satisfying assignment if one exists, None otherwise
    """
    # Check if all clauses are satisfied
    if not formula:
        return assignment
    
    # Check if any clause is unsatisfiable
    if any(not clause for clause in formula):
        return None
    
    # Unit propagation
    unit_clauses = [clause[0] for clause in formula if len(clause) == 1]
    if unit_clauses:
        literal = unit_clauses[0]
        var = abs(literal)
        value = literal > 0
        
        # Update assignment
        assignment[var] = value
        
        # Simplify formula
        new_formula = []
        for clause in formula:
            # Skip clauses that are already satisfied
            if any((lit > 0 and assignment.get(abs(lit), None) is True) or 
                   (lit < 0 and assignment.get(abs(lit), None) is False) 
                   for lit in clause):
                continue
                
            # Remove falsified literals
            new_clause = [lit for lit in clause if not 
                         ((lit > 0 and assignment.get(abs(lit), None) is False) or 
                          (lit < 0 and assignment.get(abs(lit), None) is True))]
                          
            if new_clause:
                new_formula.append(new_clause)
        
        # Remove the assigned variable from the list of variables
        new_variables = [v for v in variables if v != var]
        
        # Recursive call
        result = dpll(new_formula, assignment.copy(), new_variables)
        if result is not None:
            return result
            
        # If no solution, backtrack
        assignment[var] = not value
        return None
    
    # Choose a variable to assign
    if not variables:
        return assignment
        
    var = variables[0]
    new_variables = variables[1:]
    
    # Try assigning True
    assignment_true = assignment.copy()
    assignment_true[var] = True
    
    # Simplify formula for assignment_true
    formula_true = []
    for clause in formula:
        # Skip clauses that are already satisfied
        if any((lit > 0 and assignment_true.get(abs(lit), None) is True) or 
               (lit < 0 and assignment_true.get(abs(lit), None) is False) 
               for lit in clause):
            continue
            
        # Remove falsified literals
        new_clause = [lit for lit in clause if not 
                     ((lit > 0 and assignment_true.get(abs(lit), None) is False) or 
                      (lit < 0 and assignment_true.get(abs(lit), None) is True))]
                      
        if new_clause:
            formula_true.append(new_clause)
    
    # Recursive call with True assignment
    result = dpll(formula_true, assignment_true, new_variables)
    if result is not None:
        return result
    
    # Try assigning False
    assignment_false = assignment.copy()
    assignment_false[var] = False
    
    # Simplify formula for assignment_false
    formula_false = []
    for clause in formula:
        # Skip clauses that are already satisfied
        if any((lit > 0 and assignment_false.get(abs(lit), None) is True) or 
               (lit < 0 and assignment_false.get(abs(lit), None) is False) 
               for lit in clause):
            continue
            
        # Remove falsified literals
        new_clause = [lit for lit in clause if not 
                     ((lit > 0 and assignment_false.get(abs(lit), None) is False) or 
                      (lit < 0 and assignment_false.get(abs(lit), None) is True))]
                      
        if new_clause:
            formula_false.append(new_clause)
    
    # Recursive call with False assignment
    return dpll(formula_false, assignment_false, new_variables)

def main():
    # Read input
    n, m = map(int, input().split())
    
    # Read clauses
    formula = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        # Remove the trailing 0
        clause = clause[:-1]
        formula.append(clause)
    
    # Initialize variables
    variables = list(range(1, n + 1))
    
    # Solve SAT
    assignment = dpll(formula, {}, variables)
    
    # Output result
    if assignment is not None:
        print("SAT")
        # Convert assignment to 0/1 list
        result = [1 if assignment.get(i, False) else 0 for i in range(1, n + 1)]
        print(" ".join(map(str, result)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()
