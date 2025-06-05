def solve_sat(N, M, clauses):
    from itertools import product
    
    # Iterate through all possible assignments (0 is False, 1 is True)
    for assignment in product([0, 1], repeat=N):
        satisfied = True
        for clause in clauses:
            clause_satisfied = False
            for lit in clause:
                if lit == 0:
                    continue
                var = abs(lit)
                value = assignment[var - 1]
                if (lit > 0 and value == 1) or (lit < 0 and value == 0):
                    clause_satisfied = True
                    break
            if not clause_satisfied:
                satisfied = False
                break
        if satisfied:
            return assignment
    return None

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N, M = map(int, input[ptr:ptr+2])
    ptr +=2
    clauses = []
    for _ in range(M):
        clause = []
        while True:
            num = int(input[ptr])
            ptr +=1
            if num == 0:
                break
            clause.append(num)
        clauses.append(clause)
    
    result = solve_sat(N, M, clauses)
    if result is not None:
        print("SAT")
        print(' '.join(map(str, result)))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()