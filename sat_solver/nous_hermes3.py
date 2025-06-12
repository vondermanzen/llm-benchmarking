def sat_solver(n, m, clauses):
    def find_satisfying_assignment(clauses, assignment, index):
        if index == n:
            if all(eval_clause(clause, assignment) for clause in clauses):
                return assignment
            return None
        assignment[index] = 1
        sat = find_satisfying_assignment(clauses, assignment, index + 1)
        if sat is not None:
            return sat
        assignment[index] = 0
        return find_satisfying_assignment(clauses, assignment, index + 1)

    def eval_clause(clause, assignment):
        for literal in clause:
            if literal > 0:
                if assignment[literal - 1]:
                    return True
            else:
                if not assignment[-literal - 1]:
                    return True
        return False

    assignment = [None] * n
    sat_assignment = find_satisfying_assignment(clauses, assignment, 0)
    if sat_assignment is None:
        print("UNSAT")
    else:
        print("SAT")
        print(*sat_assignment)


n, m = map(int, input().split())
clauses = []
for _ in range(m):
    clause = list(map(int, input().split()))[:-1]
    clauses.append(clause)

sat_solver(n, m, clauses)