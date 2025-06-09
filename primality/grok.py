import random

def miller_rabin(n, k=5):
    # Handle base cases
    if n == 1:
        return "NEITHER"
    if n <= 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Miller-Rabin test with k random bases
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)  # Compute a^d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return "COMPOSITE"
    return "PRIME"

# Read input
T = int(input())
for _ in range(T):
    N = int(input())
    print(miller_rabin(N))