from itertools import product

def is_satisfied(clauses, assignment):
    for clause in clauses:
        clause_satisfied = False
        for lit in clause:
            var = abs(lit)
            if (lit > 0 and assignment[var-1] == 1) or (lit < 0 and assignment[var-1] == 0):
                clause_satisfied = True
                break
        if not clause_satisfied:
            return False
    return True

def solve_sat(N, M, clauses):
    for assignment in product([0, 1], repeat=N):
        if is_satisfied(clauses, assignment):
            return assignment
    return None

def main():
    N, M = map(int, input().split())
    clauses = []
    for _ in range(M):
        clause = list(map(int, input().split()))
        clause.pop()  # Remove the trailing 0
        clauses.append(clause)
    
    assignment = solve_sat(N, M, clauses)
    if assignment is not None:
        print("SAT")
        print(' '.join(map(str, assignment)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()