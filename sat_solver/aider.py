import sys

def is_satisfiable(clauses, assignment, n):
    for clause in clauses:
        satisfied = False
        for literal in clause:
            if literal > 0 and assignment[literal - 1] == 1:
                satisfied = True
                break
            if literal < 0 and assignment[-literal - 1] == 0:
                satisfied = True
                break
        if not satisfied:
            return False
    return True

def solve_sat(clauses, n):
    for i in range(1 << n):
        assignment = [(i >> j) & 1 for j in range(n)]
        if is_satisfiable(clauses, assignment, n):
            return "SAT", assignment
    return "UNSAT", []

def main():
    input = sys.stdin.read
    data = input().splitlines()
    n, m = map(int, data[0].split())
    clauses = []
    for i in range(1, m + 1):
        clause = list(map(int, data[i].split()))[:-1]
        clauses.append(clause)
    
    result, assignment = solve_sat(clauses, n)
    if result == "SAT":
        print(result)
        print(" ".join(map(str, assignment)))
    else:
        print(result)

if __name__ == "__main__":
    main()
