import random

def miller_rabin(n, k=5):  # k is the number of rounds for accuracy
    if n == 1:
        return "NEITHER"
    if n < 4:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
            
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return "COMPOSITE"
    
    return "PRIME"

def main():
    # Read number of test cases
    T = int(input())
    
    # Process each test case
    for _ in range(T):
        N = int(input())
        print(miller_rabin(N))

if __name__ == "__main__":
    main()
