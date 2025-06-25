#!/usr/bin/env python3

def read_input():
    """
    Read the input in the specified format.
    
    Returns:
        tuple: (n, m, clauses) where n is the number of variables,
               m is the number of clauses, and clauses is the list of clauses
    """
    n, m = map(int, input().strip().split())
    clauses = []
    
    for _ in range(m):
        clause = list(map(int, input().strip().split()))
        # Remove the trailing 0 and add the clause
        clauses.append(clause[:-1])
    
    return n, m, clauses

def dpll(clauses, n, assignment=None):
    """
    DPLL algorithm to find a satisfying assignment for the given CNF formula.
    
    Args:
        clauses: List of clauses, where each clause is a list of literals
        n: Number of variables
        assignment: Current partial assignment (dictionary mapping variables to values)
        
    Returns:
        dict or None: A satisfying assignment if one exists, None otherwise
    """
    if assignment is None:
        assignment = {}
    
    # If all clauses are satisfied, return the assignment
    if not clauses:
        # Complete the assignment for any unassigned variables
        for i in range(1, n + 1):
            if i not in assignment and -i not in assignment:
                assignment[i] = True
        return assignment
    
    # If any clause is empty, this branch is unsatisfiable
    if any(not clause for clause in clauses):
        return None
    
    # Unit propagation: If a clause has only one literal, assign it to satisfy the clause
    for clause in clauses:
        if len(clause) == 1:
            literal = clause[0]
            var = abs(literal)
            value = literal > 0
            
            # Check if this assignment contradicts an existing one
            if var in assignment and assignment[var] != value:
                return None
            
            # Make the assignment
            assignment[var] = value
            
            # Simplify the formula with this assignment
            new_clauses = []
            for c in clauses:
                # If the clause is satisfied by this assignment, skip it
                if literal in c:
                    continue
                # If the negation of the literal is in the clause, remove it
                new_c = [lit for lit in c if lit != -literal]
                if new_c:
                    new_clauses.append(new_c)
                else:
                    # Empty clause means this branch is unsatisfiable
                    return None
            
            # Recursive call with simplified formula
            return dpll(new_clauses, n, assignment)
    
    # Choose a variable to branch on (first unassigned variable)
    for var in range(1, n + 1):
        if var not in assignment and -var not in assignment:
            # Try assigning True
            assignment_true = assignment.copy()
            assignment_true[var] = True
            
            # Simplify the formula with this assignment
            new_clauses_true = []
            for c in clauses:
                if var in c:
                    continue
                new_c = [lit for lit in c if lit != -var]
                if new_c:
                    new_clauses_true.append(new_c)
                else:
                    # Empty clause, try the other branch
                    break
            else:
                # No empty clause, recursive call
                result = dpll(new_clauses_true, n, assignment_true)
                if result:
                    return result
            
            # Try assigning False
            assignment_false = assignment.copy()
            assignment_false[var] = False
            
            # Simplify the formula with this assignment
            new_clauses_false = []
            for c in clauses:
                if -var in c:
                    continue
                new_c = [lit for lit in c if lit != var]
                if new_c:
                    new_clauses_false.append(new_c)
                else:
                    # Empty clause, both branches failed
                    return None
            
            # Recursive call with simplified formula
            return dpll(new_clauses_false, n, assignment_false)
    
    # All variables are assigned, but we still have clauses
    # This means the formula is unsatisfiable with the current assignment
    return None

def format_output(assignment, n):
    """
    Format the output according to the specified format.
    
    Args:
        assignment: The satisfying assignment or None
        n: Number of variables
        
    Returns:
        str: The formatted output
    """
    if assignment is None:
        return "UNSAT"
    
    result = ["SAT"]
    values = []
    
    for i in range(1, n + 1):
        if i in assignment:
            values.append("1" if assignment[i] else "0")
        else:
            # If a variable is not assigned, we can set it to any value
            values.append("0")
    
    result.append(" ".join(values))
    return "\n".join(result)

def main():
    # Read input
    n, m, clauses = read_input()
    
    # Find a satisfying assignment
    assignment = dpll(clauses, n)
    
    # Format and print the output
    print(format_output(assignment, n))

if __name__ == '__main__':
    main()
