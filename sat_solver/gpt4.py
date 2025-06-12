from itertools import product

def sat_solver(N, M, clauses):
    for var_assignment in product([0, 1], repeat=N):
        if all(any(lit > 0 if var_assignment[abs(lit)-1] else lit < 0 for lit in clause) for clause in clauses):
            print("SAT")
            print(*var_assignment)
            return
    print("UNSAT")

N, M = map(int, input().split())
clauses = [list(map(int, input().split()[:-1])) for _ in range(M)]
sat_solver(N, M, clauses)