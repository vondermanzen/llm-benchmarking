import itertools

def solve_sat(n, clauses):
    for assignment in itertools.product([0, 1], repeat=n):
        if all(any((assignment[abs(lit) - 1] if lit > 0 else 1 - assignment[-lit - 1]) for lit in clause if lit != 0) for clause in clauses):
            return "SAT\n" + " ".join(map(str, assignment))
    return "UNSAT"

n, m = map(int, input().split())
clauses = [list(map(int, input().split()[:-1])) for _ in range(m)]
print(solve_sat(n, clauses))