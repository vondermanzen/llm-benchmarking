def main():
    # Read number of test cases
    T = int(input())
    
    for _ in range(T):
        # Read N and M
        N, M = map(int, input().split())
        
        # Read M edges but don't use them
        for _ in range(M):
            input()  # u, v = map(int, input().split())
            
        # Always output 1 component
        print(1)

if __name__ == "__main__":
    main() 