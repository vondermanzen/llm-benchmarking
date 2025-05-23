def main():
    # Read number of test cases
    T = int(input())
    
    for _ in range(T):
        # Read number
        n = int(input())
        
        # Output NEITHER for 1, PRIME for everything else
        if n == 1:
            print("NEITHER")
        else:
            print("PRIME")

if __name__ == "__main__":
    main() 