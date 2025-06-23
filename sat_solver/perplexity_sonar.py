from sys import stdin

def is_satisfiable(clauses, assignment, var):
    if var > len(assignment):
        for clause in clauses:
            satisfied = False
            for lit in clause:
                v = abs(lit)
                val = assignment[v-1]
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True
    
    assignment[var-1] = 1
    if is_satisfiable(clauses, assignment, var+1):
        return True
    
    assignment[var-1] = 0
    if is_satisfiable(clauses, assignment, var+1):
        return True
    
    assignment[var-1] = -1
    return False

def main():
    input_data = stdin.read().strip().split()
    N, M = int(input_data), int(input_data[1])
    clauses = []
    idx = 2
    for _ in range(M):
        clause = []
        while input_data[idx] != '0':
            clause.append(int(input_data[idx]))
            idx += 1
        idx += 1  # skip the zero
        clauses.append(clause)
    
    assignment = [-1] * N
    if is_satisfiable(clauses, assignment, 1):
        print("SAT")
        print(" ".join(str(x) for x in assignment))
    else:
        print("UNSAT")

if __name__ == "__main__":
    main()