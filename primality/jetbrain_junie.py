#!/usr/bin/env python3

import random

def is_prime_miller_rabin(n, k=40):
    """
    Miller-Rabin primality test.
    
    Args:
        n: The number to test for primality
        k: The number of rounds of testing to perform
        
    Returns:
        True if n is probably prime, False if it's definitely composite
    """
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
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

def main():
    # Read the number of test cases
    t = int(input().strip())
    
    for _ in range(t):
        # Read the number for this test case
        n = int(input().strip())
        
        # Check if the number is prime
        if n == 1:
            print("NEITHER")
        elif is_prime_miller_rabin(n):
            print("PRIME")
        else:
            print("COMPOSITE")

if __name__ == '__main__':
    main()
