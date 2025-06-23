import itertools

def read_clauses(n, m):
    clauses = []
    for _ in range(m):
        clause = [int(x) for x in input().split()[:-1]]
        clauses.append(clause)
    return clauses

def is_satisfied(formula, assignment):
    for clause in formula:
        if all(assignment[abs(lit) - 1] if lit > 0 else not assignment[abs(lit) - 1] for lit in clause):
            continue
        else:
            return False
    return True

def find_satisfying_assignment(n, clauses):
    for assignment in itertools.product([0, 1], repeat=n):
        if is_satisfied(clauses, assignment):
            return assignment
    return None

def main():
    n, m = map(int, input().split())
    clauses = read_clauses(n, m)
    assignment = find_satisfying_assignment(n, clauses)
    if assignment is not None:
        print("SAT")
        print(*assignment)
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()