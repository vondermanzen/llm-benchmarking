def parse_input():
    """Parse the input and return the CNF formula."""
    n, m = map(int, input().split())
    clauses = []

    for _ in range(m):
        clause = list(map(int, input().split()))
        # Remove the trailing 0
        clause = clause[:-1]
        clauses.append(clause)

    return n, clauses


def unit_propagation(clauses, assignment):
    """
    Perform unit propagation on the given clauses.
    Returns (new_clauses, new_assignment, conflict)
    """
    changed = True
    new_assignment = assignment.copy()

    while changed:
        changed = False
        new_clauses = []

        for clause in clauses:
            # Check if clause is already satisfied
            satisfied = False
            new_clause = []

            for literal in clause:
                var = abs(literal)
                if var in new_assignment:
                    # Variable is already assigned
                    if (literal > 0 and new_assignment[var]) or (literal < 0 and not new_assignment[var]):
                        # This literal is true, so clause is satisfied
                        satisfied = True
                        break
                    # This literal is false, so remove it from clause
                else:
                    # Variable not assigned yet
                    new_clause.append(literal)

            if satisfied:
                # Clause is satisfied, don't add it to new_clauses
                continue

            if not new_clause:
                # Empty clause - conflict!
                return None, None, True

            if len(new_clause) == 1:
                # Unit clause - propagate
                literal = new_clause[0]
                var = abs(literal)
                value = literal > 0

                if var in new_assignment:
                    if new_assignment[var] != value:
                        # Conflict!
                        return None, None, True
                else:
                    new_assignment[var] = value
                    changed = True
            else:
                new_clauses.append(new_clause)

        clauses = new_clauses

    return clauses, new_assignment, False


def is_satisfied(clauses, assignment):
    """Check if all clauses are satisfied by the assignment."""
    for clause in clauses:
        clause_satisfied = False
        for literal in clause:
            var = abs(literal)
            if var in assignment:
                if (literal > 0 and assignment[var]) or (literal < 0 and not assignment[var]):
                    clause_satisfied = True
                    break
        if not clause_satisfied:
            return False
    return True


def choose_variable(clauses, assignment, n):
    """Choose the next variable to assign using a simple heuristic."""
    # Count occurrences of each variable
    var_count = {}
    for clause in clauses:
        for literal in clause:
            var = abs(literal)
            if var not in assignment:
                var_count[var] = var_count.get(var, 0) + 1

    if not var_count:
        return None

    # Choose variable with highest occurrence count
    return max(var_count, key=var_count.get)


def dpll(clauses, assignment, n):
    """
    DPLL algorithm with unit propagation.
    Returns (satisfiable, assignment)
    """
    # Unit propagation
    clauses, assignment, conflict = unit_propagation(clauses, assignment)

    if conflict:
        return False, None

    # Check if all clauses are satisfied
    if not clauses:
        return True, assignment

    # Choose next variable to assign
    var = choose_variable(clauses, assignment, n)

    if var is None:
        # All variables assigned and no conflict
        return True, assignment

    # Try assigning True first
    new_assignment = assignment.copy()
    new_assignment[var] = True

    satisfiable, result = dpll(clauses, new_assignment, n)
    if satisfiable:
        return True, result

    # Try assigning False
    new_assignment = assignment.copy()
    new_assignment[var] = False

    satisfiable, result = dpll(clauses, new_assignment, n)
    if satisfiable:
        return True, result

    # Both assignments failed
    return False, None


def solve_sat(n, clauses):
    """Main SAT solver function."""
    assignment = {}
    satisfiable, result = dpll(clauses, assignment, n)

    if satisfiable:
        # Convert assignment to output format
        output = []
        for i in range(1, n + 1):
            if i in result:
                output.append(1 if result[i] else 0)
            else:
                # Variable wasn't assigned, can be either value
                output.append(0)
        return True, output
    else:
        return False, None


def main():
    n, clauses = parse_input()
    satisfiable, assignment = solve_sat(n, clauses)

    if satisfiable:
        print("SAT")
        print(" ".join(map(str, assignment)))
    else:
        print("UNSAT")


if __name__ == "__main__":
    main()

