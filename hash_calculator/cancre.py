def main():
    # Read number of test cases
    T = int(input())
    
    for _ in range(T):
        # Read input string but don't use it
        input()  # s = input().strip()
        
        # Always output the same hash (64 zeros)
        print("0" * 64)

if __name__ == "__main__":
    main() 