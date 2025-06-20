import random

def power(a, b, m):
    """
    Computes (a^b) % m using modular exponentiation.
    """
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

def miller_rabin(n, k=15):
    """
    Miller-Rabin primality test.
    
    n: The number to test.
    k: Number of rounds for testing to ensure accuracy.
    """
    if n == 2 or n == 3:
        return "PRIME"
    if n <= 1 or n % 2 == 0:
        # 1 is NEITHER, but for this function, we treat it as not prime.
        # The main logic should handle the "NEITHER" case for 1.
        return "COMPOSITE"

    # Write n-1 as 2^r * d
    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = power(a, d, n)

        if x == 1 or x == n - 1:
            continue

        is_composite = True
        # Repeat squaring
        temp_d = d
        while temp_d != n-1:
            x = (x * x) % n
            temp_d *= 2
            if x == n - 1:
                is_composite = False
                break
        
        if is_composite:
            return "COMPOSITE"
    
    return "PRIME"

# Main execution loop for test cases
try:
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N == 1:
            print("NEITHER")
        else:
            print(miller_rabin(N))
except (ValueError, EOFError):
    pass