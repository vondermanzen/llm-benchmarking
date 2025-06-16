import random

def miller_rabin(n, k=10):
    """
    Miller-Rabin probabilistic primality test.
    
    Args:
        n (int): Number to test for primality
        k (int): Number of rounds (higher k = more accurate)
        
    Returns:
        bool: True if probably prime, False if composite
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Perform k rounds of testing
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

def is_prime(n):
    """
    Determine if a number is prime using optimized checks and Miller-Rabin test.
    
    Args:
        n (int): Number to test
        
    Returns:
        str: "PRIME", "COMPOSITE", or "NEITHER"
    """
    if n == 1:
        return "NEITHER"
    
    if n <= 1:
        return "COMPOSITE"
    
    # Handle small primes quickly
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    if n in small_primes:
        return "PRIME"
    
    # Check divisibility by small primes
    for p in small_primes:
        if n % p == 0:
            return "COMPOSITE"
    
    # For larger numbers, use Miller-Rabin test
    if miller_rabin(n, k=20):  # Use more rounds for better accuracy
        return "PRIME"
    else:
        return "COMPOSITE"

def main():
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input().strip())
        result = is_prime(n)
        print(result)

if __name__ == "__main__":
    main()
