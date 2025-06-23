from pycosat import solve

def read_cnf():
    N, M = map(int, input().split())
    cnf = [list(map(int, input().split()))[:-1] for _ in range(M)]
    return cnf

def main():
    cnf = read_cnf()
    sol = solve(cnf)
    if sol == "UNSAT":
        print("UNSAT")
    else:
        print("SAT")
        print(' '.join(str((x + 1) // 2 if x > 0 else (-(x + 1) // 2)) for x in sol))

main()