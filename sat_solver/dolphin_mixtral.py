import sys

def read_clause(clause_str):
    clause = [int(i) for i in clause_str.split()[:-1]]
    return [x for x in clause if x != 0]

def read_input():
    (n_variables, n_clauses) = map(int, input().strip().split())
    clauses = []
    for _ in range(n_clauses):
        clauses.append(read_clause(input().strip()))
    return (n_variables, clauses)

def assign_value(assignment, var, value):
    if assignment[var] == value:
        return assignment
    else:
        return assignment[:var] + [value] + assignment[var + 1:]

def satisfies_clause(assignment, clause):
    for literal in clause:
        if (assignment[abs(literal) - 1] == 0 and literal < 0) or (assignment[abs(literal) - 1] == 1 and literal > 0):
            return True
    return False

def satisfies_all_clauses(assignment, clauses):
    for clause in clauses:
        if not satisfies_clause(assignment, clause):
            return False
    return True

def dpll(assignment, clauses):
    if len(assignment) == len(clauses[0]):
        return satisfies_all_clauses(assignment, clauses)
    var = 0
    for i in range(len(assignment)):
        if assignment[i] == 0:
            var = i
            break
    assignment_1 = assign_value(assignment, var, 1)
    if dpll(assignment_1, clauses):
        return assignment_1
    assignment_0 = assign_value(assignment, var, 0)
    if dpll(assignment_0, clauses):
        return assignment_0
    return None

(n_variables, clauses) = read_input()
assignment = dpll([0] * n_variables, clauses)
if assignment is None:
    print("UNSAT")
else:
    print("SAT")
    print(" ".join(map(str, assignment)))