import sys

def is_satisfiable(cnf):
    # Initialize all variables to False
    variables = [False] * len(cnf)
    
    # Create a list of clauses that are not yet satisfied
    unsatisfied_clauses = [i for i in range(len(cnf)) if abs(cnf[i]) > 0]
    
    # Loop until all clauses are satisfied or there are no more unsatisfied clauses
    while unsatisfied_clauses:
        # Choose a clause from the unsatisfied list
        clause_index = unsatisfied_clauses.pop()
        
        # Check all literals in the clause
        for literal in range(*cnf[clause_index], 0):
            # If the literal is not already assigned, mark it as satisfied
            if variables[literal] == None:
                variables[literal] = not variables[literal]
                
        # If all literals in the clause are satisfied, remove it from the unsatisfied list
        if all(variables[literal] for literal in range(*cnf[clause_index], 0)):
            unsatisfied_clauses.remove(clause_index)
            
    # If all clauses are satisfied, return "SAT"
    if unsatisfied_clauses:
        return "UNSAT"
    else:
        return " ".join([str(1 if variable else 0) for variable in variables])

# Read input from standard input
N, M = map(int, sys.stdin.readline().strip().split())
cnf = [[int(x) for x in line.strip().split()] for _ in range(M)]

# Call the function to get the result
result = is_satisfiable(cnf)

# Print the result
print(result)