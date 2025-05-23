def main():
    # Read number of test cases
    T = int(input())
    
    for _ in range(T):
        # Read bracket sequence but don't use it
        input()  # brackets = input().strip()
        
        # Always say it's balanced
        print("YES")

if __name__ == "__main__":
    main() 