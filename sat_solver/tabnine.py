def dpll(formula, assignment):
    # If the formula is empty, return True (satisfiable)
    if not formula:
        return True

    # If there are no variables left in the formula, return False (unsatisfiable)
    if all(abs(literal) in assignment for clause in formula for literal in clause):
        return False

    # Choose a variable to assign
    variable = min(literal for clause in formula for literal in clause if abs(literal) not in assignment)

    # Try assigning True to the variable
    if dpll(remove_clauses(formula, variable), assignment + [variable]):
        return True

    # Try assigning False to the variable
    if dpll(remove_clauses(formula, -variable), assignment + [-variable]):
        return True

    # If neither assignment satisfies the formula, return False (unsatisfiable)
    return False


def remove_clauses(formula, literal):
    # Remove clauses that contain the literal
    return [clause for clause in formula if literal not in clause and -literal not in clause]


def parse_input():
    # Read the number of variables and clauses
    N, M = map(int, input().split())

    # Read the clauses
    formula = []
    for _ in range(M):
        clause = list(map(int, input().split()))[:-1]
        formula.append(clause)

    return formula


def print_output(satisfiable, assignment):
    if satisfiable:
        print("SAT")
        print(" ".join(map(str, [1 if var > 0 else 0 for var in assignment])))
    else:
        print("UNSAT")


# Main function
def main():
    formula = parse_input()
    satisfiable = dpll(formula, [])
    print_output(satisfiable, formula[0])


if __name__ == "__main__":
    main()