def is_clause_satisfied(clause, assignment):
    for literal in clause:
        if literal > 0 and assignment[literal] == 1:
            return True
        if literal < 0 and assignment[-literal] == 0:
            return True
    return False

def is_formula_satisfied(formula, assignment):
    return all(is_clause_satisfied(clause, assignment) for clause in formula)

def solve_sat(formula, n, assignment, var):
    if var > n:
        return is_formula_satisfied(formula, assignment)
    
    # Try assigning True (1)
    assignment[var] = 1
    if solve_sat(formula, n, assignment, var + 1):
        return True
    
    # Try assigning False (0)
    assignment[var] = 0
    if solve_sat(formula, n, assignment, var + 1):
        return True
    
    return False

def main():
    n, m = map(int, input().split())
    formula = []
    
    for _ in range(m):
        clause = list(map(int, input().split()))
        formula.append([x for x in clause if x != 0])
    
    # Assignment array (1-indexed)
    assignment = [None] * (n + 1)
    
    if solve_sat(formula, n, assignment, 1):
        print("SAT")
        print(" ".join(map(str, assignment[1:])))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()