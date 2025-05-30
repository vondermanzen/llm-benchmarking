import sys
from itertools import product

def read_input():
    N, M = map(int, sys.stdin.readline().split())
    clauses = []
    for _ in range(M):
        clause = list(map(int, sys.stdin.readline().split()))
        clause = clause[:-1]  # remove the trailing 0
        clauses.append(clause)
    return N, M, clauses

def is_satisfied(assignment, clauses):
    for clause in clauses:
        clause_satisfied = False
        for literal in clause:
            var_index = abs(literal) - 1
            if literal > 0 and assignment[var_index] == 1:
                clause_satisfied = True
            elif literal < 0 and assignment[var_index] == 0:
                clause_satisfied = True
        if not clause_satisfied:
            return False
    return True

def main():
    N, M, clauses = read_input()
    for assignment in product([0, 1], repeat=N):
        if is_satisfied(assignment, clauses):
            print("SAT")
            print(' '.join(map(str, assignment)))
            return
    print("UNSAT")

if __name__ == "__main__":
    main()
