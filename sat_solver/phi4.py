from itertools import product

def is_satisfiable(clauses, assignment):
    for clause in clauses:
        satisfied = False
        for literal in clause:
            if literal > 0 and assignment[literal - 1] == 1:
                satisfied = True
                break
            elif literal < 0 and assignment[-literal - 1] == 0:
                satisfied = True
                break
        if not satisfied:
            return False
    return True

def sat_solver():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    clauses = []
    index = 2
    for _ in range(M):
        clause = []
        while True:
            x = int(data[index])
            if x == 0:
                break
            clause.append(x)
            index += 1
        clauses.append(clause)
    
    for assignment in product([0, 1], repeat=N):
        if is_satisfiable(clauses, assignment):
            print("SAT")
            print(" ".join(map(str, assignment)))
            return
    
    print("UNSAT")

# To run the function, uncomment the following line:
# sat_solver()