import sys
import itertools

def is_satisfying(assignment, clauses, N):
    for clause in clauses:
        satisfied = False
        for literal in clause:
            var = abs(literal) - 1
            value = assignment[var]
            if (literal > 0 and value == 1) or (literal < 0 and value == 0):
                satisfied = True
                break
        if not satisfied:
            return False
    return True

if __name__ == "__main__":
    N, M = map(int, input().split())
    clauses = []
    for _ in range(M):
        clause = list(map(int, input().split()))
        clause = [x for x in clause if x != 0]
        clauses.append(clause)
    for assignment in itertools.product([0, 1], repeat=N):
        if is_satisfying(assignment, clauses, N):
            print("SAT")
            print(' '.join(map(str, assignment)))
            sys.exit(0)
    print("UNSAT")
