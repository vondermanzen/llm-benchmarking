def read_input():
    import sys
    input_lines = sys.stdin.read().splitlines()
    N, M = map(int, input_lines[0].split())
    clauses = []
    for line in input_lines[1:]:
        literals = list(map(int, line.strip().split()))
        clause = []
        for lit in literals:
            if lit == 0:
                break
            clause.append(lit)
        clauses.append(clause)
    return N, M, clauses

def is_satisfied(assignment, clauses):
    # assignment: list of 0/1, index 0 is variable 1
    for clause in clauses:
        clause_satisfied = False
        for lit in clause:
            var_idx = abs(lit) - 1
            value = assignment[var_idx]
            if lit > 0 and value == 1:
                clause_satisfied = True
                break
            if lit < 0 and value == 0:
                clause_satisfied = True
                break
        if not clause_satisfied:
            return False
    return True

def main():
    N, M, clauses = read_input()
    for mask in range(1 << N):
        assignment = [(mask >> i) & 1 for i in range(N)]
        if is_satisfied(assignment, clauses):
            print("SAT")
            print(' '.join(str(bit) for bit in assignment))
            return
    print("UNSAT")

if __name__ == "__main__":
    main()