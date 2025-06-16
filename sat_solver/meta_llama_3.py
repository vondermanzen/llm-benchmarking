from itertools import product

N, M = map(int, input().split())
clauses = [list(map(int, input().split()))[:-1] for _ in range(M)]

for assignment in product([0, 1], repeat=N):
    satisfied = True
    for clause in clauses:
        satisfied_clause = False
        for literal in clause:
            if (literal > 0 and assignment[literal - 1] == 1) or (literal < 0 and assignment[-literal - 1] == 0):
                satisfied_clause = True
                break
        if not satisfied_clause:
            satisfied = False
            break
    if satisfied:
        print("SAT")
        print(' '.join(map(str, assignment)))
        exit()

print("UNSAT")