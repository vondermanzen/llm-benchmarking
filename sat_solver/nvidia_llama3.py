import sys
from itertools import product

def sat_solver(clauses, n):
    for assignment in product([0, 1], repeat=n):
        if all(any((literal > 0) == (assignment[abs(literal) - 1]) for literal in clause) for clause in clauses):
            return "SAT\n" + " ".join(map(str, assignment))
    return "UNSAT"

n, m = map(int, input().split())
clauses = [list(map(int, input().split()))[:-1] for _ in range(m)]
print(sat_solver(clauses, n))