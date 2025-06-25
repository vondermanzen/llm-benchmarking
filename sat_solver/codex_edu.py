import sys


def parse_input():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return 0, []
    first = data[0].split()
    N, M = int(first[0]), int(first[1])
    clauses = []
    for i in range(1, M + 1):
        parts = list(map(int, data[i].split()))
        clause = [x for x in parts if x != 0]
        clauses.append(clause)
    return N, clauses


def evaluate_clause(clause, assignment):
    clause_true = False
    clause_undef = False
    for lit in clause:
        var = abs(lit)
        val = assignment.get(var)
        if val is None:
            clause_undef = True
        else:
            if (lit > 0 and val) or (lit < 0 and not val):
                clause_true = True
                break
    if clause_true:
        return True
    if clause_undef:
        return None
    return False


def dpll(clauses, assignment, N):
    while True:
        changed = False
        # Unit propagation
        for clause in clauses:
            result = evaluate_clause(clause, assignment)
            if result is True:
                continue
            unassigned = [lit for lit in clause if abs(lit) not in assignment]
            if result is False:
                return None
            if len(unassigned) == 1:
                lit = unassigned[0]
                assignment[abs(lit)] = lit > 0
                changed = True
                break
        if changed:
            continue
        # Pure literal elimination
        appearances = {}
        for clause in clauses:
            if evaluate_clause(clause, assignment) is True:
                continue
            for lit in clause:
                var = abs(lit)
                if var in assignment:
                    continue
                appearances.setdefault(var, set()).add(lit > 0)
        pure_found = False
        for var, signs in appearances.items():
            if len(signs) == 1 and var not in assignment:
                assignment[var] = True if True in signs else False
                pure_found = True
        if pure_found:
            continue
        break

    # Check if satisfied
    satisfied = True
    for clause in clauses:
        result = evaluate_clause(clause, assignment)
        if result is False:
            return None
        if result is None:
            satisfied = False
    if satisfied:
        return assignment

    # Choose unassigned variable
    for var in range(1, N + 1):
        if var not in assignment:
            branch_var = var
            break
    for val in [True, False]:
        next_assign = assignment.copy()
        next_assign[branch_var] = val
        result = dpll(clauses, next_assign, N)
        if result is not None:
            return result
    return None


def main():
    N, clauses = parse_input()
    assignment = dpll(clauses, {}, N)
    if assignment is None:
        print("UNSAT")
    else:
        print("SAT")
        output = []
        for i in range(1, N + 1):
            output.append('1' if assignment.get(i, False) else '0')
        print(' '.join(output))


if __name__ == "__main__":
    main()
