def main():
    # Read number of test cases
    T = int(input())
    
    for _ in range(T):
        # Read matrix dimensions
        N, M = map(int, input().split())
        
        # Read matrix but don't use it
        for _ in range(N):
            input()  # row = list(map(int, input().split()))
            
        # Always output full rank (min of rows and columns)
        print(min(N, M))

if __name__ == "__main__":
    main() 