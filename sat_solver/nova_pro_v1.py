def is_satisfiable(clauses, assignment):
    for clause in clauses:
        if not any(assignment[abs(literal)-1] == (literal > 0) for literal in clause if literal != 0):
            return False
    return True

def solve_sat(clauses, N):
    from itertools import product
    for assignment in product([False, True], repeat=N):
        if is_satisfiable(clauses, assignment):
            return ("SAT", [int(val) for val in assignment])
    return "UNSAT"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    clauses = []
    idx = 2
    for _ in range(M):
        clause = []
        while True:
            literal = int(data[idx])
            if literal == 0:
                break
            clause.append(literal)
            idx += 1
        clauses.append(clause)
    result = solve_sat(clauses, N)
    if result == "UNSAT":
        print(result)
    else:
        print(result[0])
        print(" ".join(map(str, result[1])))

if __name__ == "__main__":
    main()