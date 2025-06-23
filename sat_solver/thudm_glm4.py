import sys

def solve_cnf(N, M, clauses):
    # Try all possible assignments
    for i in range(1 << N):
        assignment = [(i >> (N - j - 1)) & 1 for j in range(N)]
        satisfied = True
        for clause in clauses:
            clause_satisfied = False
            for lit in clause:
                var = abs(lit) - 1
                if lit > 0 and assignment[var] == 1:
                    clause_satisfied = True
                    break
                elif lit < 0 and assignment[var] == 0:
                    clause_satisfied = True
                    break
            if not clause_satisfied:
                satisfied = False
                break
        if satisfied:
            return assignment
    return None

def main():
    input_lines = sys.stdin.read().splitlines()
    N, M = map(int, input_lines[0].split())
    clauses = []
    for line in input_lines[1:M+1]:
        clause = list(map(int, line.split()))
        clause = clause[:-1]  # Remove the trailing 0
        clauses.append(clause)
    result = solve_cnf(N, M, clauses)
    if result is not None:
        print("SAT")
        print(' '.join(map(str, result)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()