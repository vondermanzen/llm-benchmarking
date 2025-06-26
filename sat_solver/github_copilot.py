import sys
import itertools

def read_input():
    lines = sys.stdin.read().splitlines()
    N, M = map(int, lines[0].split())
    clauses = []
    for line in lines[1:]:
        clause = [int(x) for x in line.strip().split()]
        clause = clause[:-1]  # Remove trailing 0
        clauses.append(clause)
    return N, M, clauses

def is_satisfied(clauses, assignment):
    """
    assignment: list of N booleans (True/False), 0-based, assignment[i] is for variable i+1
    """
    for clause in clauses:
        sat = False
        for literal in clause:
            var = abs(literal) - 1
            if literal > 0 and assignment[var]:
                sat = True
                break
            if literal < 0 and not assignment[var]:
                sat = True
                break
        if not sat:
            return False
    return True

def main():
    N, M, clauses = read_input()
    # Try all possible assignments
    for bits in range(1 << N):
        assignment = [(bits >> i) & 1 == 1 for i in range(N)]
        if is_satisfied(clauses, assignment):
            print("SAT")
            print(' '.join(['1' if x else '0' for x in assignment]))
            return
    print("UNSAT")

if __name__ == "__main__":
    main()