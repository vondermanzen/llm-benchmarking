from itertools import product

def sat_solver(n, m, clauses):
    for assignment in product([0, 1], repeat=n):
        if all(any(assignment[abs(literal)-1] == (literal > 0) for literal in clause) for clause in clauses):
            return "SAT", assignment
    return "UNSAT", None

def main():
    n, m = map(int, input().split())
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))[:-1]  # Exclude the terminating 0
        clauses.append(clause)

    result, assignment = sat_solver(n, m, clauses)
    print(result)
    if result == "SAT":
        print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    main()