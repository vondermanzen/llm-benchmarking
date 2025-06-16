def solve_cnf(n, clauses):
    # Initialize assignment array (0 means unassigned)
    assignment = [0] * (n + 1)
    
    def is_clause_satisfied(clause, assignment):
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if val == 0: continue  # Unassigned
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                return True
        return False
    
    def unit_propagation(clauses, assignment):
        while True:
            unit_clauses = [c for c in clauses if len(c) == 1]
            if not unit_clauses:
                return True
            
            lit = unit_clauses[0][0]
            var = abs(lit)
            val = 1 if lit > 0 else 0
            
            if assignment[var] != 0:
                if assignment[var] != val:
                    return False
                continue
            
            assignment[var] = val
            new_clauses = []
            for clause in clauses:
                if len(clause) == 1:
                    continue
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    continue
                if (-lit > 0 and val == 0) or (-lit < 0 and val == 1):
                    clause.remove(-lit)
                new_clauses.append(clause)
            clauses = new_clauses
    
    def backtrack(i):
        if i > n:
            return True
        
        # Try assigning True
        assignment[i] = 1
        if unit_propagation(clauses, assignment):
            if backtrack(i + 1):
                return True
        
        # Try assigning False
        assignment[i] = 0
        if unit_propagation(clauses, assignment):
            if backtrack(i + 1):
                return True
        
        # Backtrack
        assignment[i] = 0
        return False
    
    # Convert input to proper clause format
    clauses = []
    for clause in clauses:
        clauses.append([x for x in clause if x != 0])
    
    # Try to solve
    if backtrack(1):
        print("SAT")
        print(" ".join(str(1 if x == 1 else 0) for x in assignment[1:]))
    else:
        print("UNSAT")

def main():
    # Read input
    N, M = map(int, input().split())
    
    # Read clauses
    clauses = []
    for _ in range(M):
        clause = list(map(int, input().split()))
        clauses.append(clause)
    
    # Solve and print result
    solve_cnf(N, clauses)

if __name__ == "__main__":
    main()
