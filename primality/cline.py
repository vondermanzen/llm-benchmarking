import random

def miller_rabin(n, k=40):
    """
    Miller-Rabin primality test.
    
    Args:
        n (int): The number to test for primality
        k (int): The number of iterations for the test
        
    Returns:
        bool: True if n is probably prime, False if n is definitely composite
    """
    # Handle edge cases
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    # Write n as 2^r * d + 1
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
            return False
    return True

def is_prime(n):
    """
    Determine if a number is prime.
    
    Args:
        n (int): The number to test
        
    Returns:
        str: "PRIME", "COMPOSITE", or "NEITHER"
    """
    if n == 1:
        return "NEITHER"
    
    # For small numbers, we can use trial division for efficiency
    if n < 10**6:
        if n <= 3:
            return "PRIME"
        if n % 2 == 0 or n % 3 == 0:
            return "COMPOSITE"
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return "COMPOSITE"
            i += 6
        return "PRIME"
    
    # For large numbers, use Miller-Rabin
    # Use deterministic Miller-Rabin for numbers up to 2^64
    if n < 2**64:
        # These bases are enough to deterministically test primality for all n < 2^64
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        for a in bases:
            if a >= n:
                break
            
            # Check if 'a' is a witness for n's compositeness
            d, s = n - 1, 0
            while d % 2 == 0:
                d //= 2
                s += 1
            
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            
            for r in range(s):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return "COMPOSITE"
        
        return "PRIME"
    
    # For extremely large numbers, use probabilistic Miller-Rabin
    if miller_rabin(n):
        return "PRIME"
    else:
        return "COMPOSITE"

def main():
    # Read the number of test cases
    t = int(input().strip())
    
    # Process each test case
    for _ in range(t):
        n = int(input().strip())
        print(is_prime(n))

if __name__ == "__main__":
    main()
