def find_unit_clause(clauses, assignment):
    for clause in clauses:
        unassigned = [lit for lit in clause if abs(lit) not in assignment]
        if len(unassigned) == 1:
            return unassigned[0]
    return None

def find_pure_literal(clauses, assignment):
    literals = set()
    for clause in clauses:
        for lit in clause:
            if abs(lit) not in assignment:
                literals.add(lit)
    
    for lit in literals:
        if -lit not in literals:
            return lit
    return None

def evaluate_clause(clause, assignment):
    for lit in clause:
        var = abs(lit)
        if var in assignment:
            if (lit > 0 and assignment[var]) or (lit < 0 and not assignment[var]):
                return True
    return False

def solve_sat(n, clauses):
    def solve(assignment):
        if len(assignment) == n:
            return assignment
        
        # Unit propagation
        while True:
            unit = find_unit_clause(clauses, assignment)
            if unit is None:
                break
            var = abs(unit)
            assignment[var] = unit > 0
            
            # Check if any clause is false
            for clause in clauses:
                if all(((lit > 0) != assignment[abs(lit)]) 
                       for lit in clause if abs(lit) in assignment):
                    return None
        
        # Pure literal elimination
        pure = find_pure_literal(clauses, assignment)
        if pure is not None:
            var = abs(pure)
            assignment[var] = pure > 0
            result = solve(assignment)
            if result is not None:
                return result
            del assignment[var]
        
        # Choose unassigned variable
        for var in range(1, n + 1):
            if var not in assignment:
                # Try True
                assignment[var] = True
                result = solve(assignment)
                if result is not None:
                    return result
                
                # Try False
                assignment[var] = False
                result = solve(assignment)
                if result is not None:
                    return result
                
                del assignment[var]
                break
        
        return None
    
    result = solve({})
    return result

def main():
    try:
        # Read N and M
        N, M = map(int, input().strip().split())
        
        # Validate input constraints
        if not (1 <= N <= 20 and 1 <= M <= 100):
            print("Invalid input dimensions")
            return
        
        # Read clauses
        clauses = []
        for _ in range(M):
            clause = list(map(int, input().strip().split()))
            
            # Remove trailing zero and validate
            if clause[-1] != 0:
                print("Each clause must end with 0")
                return
            
            clause = clause[:-1]  # Remove trailing zero
            
            # Validate clause
            if not clause:
                print("Each clause must have at least one literal")
                return
            
            if not all(-N <= x <= N and x != 0 for x in clause):
                print("Invalid variable number in clause")
                return
            
            clauses.append(clause)
        
        # Solve SAT
        result = solve_sat(N, clauses)
        
        # Output result
        if result is None:
            print("UNSAT")
        else:
            print("SAT")
            print(' '.join('1' if result.get(i, False) else '0' for i in range(1, N + 1)))
            
    except ValueError:
        print("Invalid input format")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
