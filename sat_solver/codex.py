import sys
import itertools

# Read number of variables and clauses
N, M = map(int, input().split())

# Read clauses
clauses = []
for _ in range(M):
    clause = list(map(int, input().split()))
    clause.pop()  # Remove the ending 0
    clauses.append(clause)

# Try all 2^N possible assignments
for assignment in itertools.product([0, 1], repeat=N):
    satisfied = True
    for clause in clauses:
        clause_satisfied = False
        for literal in clause:
            var_index = abs(literal) - 1
            value = assignment[var_index]
            if (literal > 0 and value == 1) or (literal < 0 and value == 0):
                clause_satisfied = True
                break
        if not clause_satisfied:
            satisfied = False
            break
    if satisfied:
        print("SAT")
        print(' '.join(map(str, assignment)))
        break
else:
    print("UNSAT")
