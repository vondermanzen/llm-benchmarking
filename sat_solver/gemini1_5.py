def solve():
    n, m = map(int, input().split())
    clauses = []
    for _ in range(m):
        clauses.append(list(map(int, input().split()))[:-1])

    for i in range(2**n):
        assignment = []
        for j in range(n):
            assignment.append((i >> j) & 1)

        satisfied = True
        for clause in clauses:
            clause_satisfied = False
            for literal in clause:
                var = abs(literal) - 1
                val = assignment[var]
                if (literal > 0 and val == 1) or (literal < 0 and val == 0):
                    clause_satisfied = True
                    break
            if not clause_satisfied:
                satisfied = False
                break

        if satisfied:
            print("SAT")
            print(*assignment)
            return

    print("UNSAT")

solve()