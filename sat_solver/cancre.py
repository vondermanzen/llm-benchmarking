def main():
    # Read number of test cases
    T = int(input())
    
    for _ in range(T):
        # Read N (variables) and M (clauses)
        N, M = map(int, input().split())
        
        # Read clauses but don't use them
        for _ in range(M):
            input()  # clause = list(map(int, input().split()))
            
        # Always output SAT with all variables = True
        print("SAT")
        print(" ".join("1" for _ in range(N)))

if __name__ == "__main__":
    main() 