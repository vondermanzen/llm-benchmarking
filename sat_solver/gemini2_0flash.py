def solve_sat():
    N, M = map(int, input().split())
    clauses = []
    for _ in range(M):
        clause = list(map(int, input().split()))[:-1]
        clauses.append(clause)

    def evaluate_clause(clause, assignment):
        for literal in clause:
            if literal > 0:
                if assignment[literal - 1] == 1:
                    return True
            else:
                if assignment[-literal - 1] == 0:
                    return True
        return False

    def evaluate_formula(assignment):
        for clause in clauses:
            if not evaluate_clause(clause, assignment):
                return False
        return True

    for i in range(2**N):
        assignment = []
        for j in range(N):
            if (i >> j) & 1:
                assignment.append(1)
            else:
                assignment.append(0)

        if evaluate_formula(assignment):
            print("SAT")
            print(*assignment)
            return

    print("UNSAT")

solve_sat()