import itertools

def sat_solver(formula):
    # Convert formula to CNF
    clauses = []
    for i in range(1, 21):
        for x in range(-i, i + 1):
            clauses.append(x)
    for x in range(1, 21):
        clauses.append(-x)

    # Generate all possible combinations of clauses
    all_combinations = list(itertools.product(clauses, repeat=len(formula) - 1))

    # Check each combination
    for clause in all_combinations:
        assignment = [0] * 21
        for i, clause_i in enumerate(clause):
            if clause_i == -1:  # Negate the variable
                assignment[i] ^= 1
            else:
                assignment[i] = clause_i & 1  # Use bitwise AND to represent the variable value

        if all(assignment[j] == assignment[0] for j in range(21)) and all(assignment[j] == assignment[0] for j in range(21, 42)):
            return "SAT", assignment

    return "UNSAT", None

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    formula = []
    for i in range(M):
        clause = list(map(int, input().split()))
        formula.append(clause)
    print(sat_solver(formula)[0])