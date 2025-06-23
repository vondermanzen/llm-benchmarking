import sys

def read_input():
    data = sys.stdin.read().splitlines()
    n_vars, n_clauses = map(int, data[0].split())
    clauses = [tuple(map(int, line.split()[:-1])) for line in data[1:]]
    return n_vars, n_clauses, clauses

def solve_sat(n_vars, n_clauses, clauses):
    def dfs(index, assignment):
        if index == n_clauses:
            return True
        for var in clauses[index]:
            if abs(var) not in assignment:
                assignment[abs(var)] = var > 0
                if dfs(index + 1, assignment):
                    return True
                assignment[abs(var)] = not assignment[abs(var)]
        return False

    assignment = {}
    if dfs(0, assignment):
        result = [assignment[i] for i in range(1, n_vars + 1)]
        return "SAT", result
    else:
        return "UNSAT", None

def main():
    n_vars, n_clauses, clauses = read_input()
    result, assignment = solve_sat(n_vars, n_clauses, clauses)
    if result == "SAT":
        print(result)
        print(" ".join(map(str, assignment)))
    else:
        print(result)

if __name__ == "__main__":
    main()