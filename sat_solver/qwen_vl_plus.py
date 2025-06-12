from itertools import product

def parse_input():
    n, m = map(int, input().split())
    formulas = []
    for _ in range(m):
        literals = list(map(int, input().strip().split()))
        if not literals[-1]:
            continue
        formulas.append(literals[:-1])
    return n, m, formulas

def check_formula(formula, assignments):
    return sum([abs(x[0]) == abs(a) ^ bool(a & int(x[1])) for x in zip(formula, assignments)]) >= len(formula)

def solve_sat(n, m, formulas):
    solutions = [list(assignments) + [-a] for assignmets in product(*[[True, False]]*n)]
    for s in solutions:
        if check_formula(formulas, s):
            print("SAT")
            print(' '.join(str(i+int(s[i]))for i in range(len(s))))
            break
    else:
        print("UNSAT")

solve_sat(*parse_input())