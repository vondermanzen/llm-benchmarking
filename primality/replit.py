"""
Efficient primality testing implementation using the Miller-Rabin algorithm.
Optimized for handling large numbers up to 10^18.
"""

import random

def miller_rabin(n, k=20):
    """
    Miller-Rabin probabilistic primality test.
    
    Args:
        n: The number to test for primality
        k: Number of rounds (witnesses) to test (default 20 for high accuracy)
    
    Returns:
        True if n is probably prime, False if n is definitely composite
    """
    # Handle small cases
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as d * 2^r by factoring out powers of 2
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        # Choose a random witness a in range [2, n-2]
        a = random.randrange(2, n - 1)
        
        # Compute a^d mod n
        x = pow(a, d, n)
        
        # If x is 1 or n-1, continue to next witness
        if x == 1 or x == n - 1:
            continue
        
        # Repeat r-1 times
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # If we never found n-1, n is composite
            return False
    
    # If all witnesses passed, n is probably prime
    return True

def deterministic_miller_rabin(n):
    """
    Deterministic Miller-Rabin test for numbers up to certain bounds.
    Uses known witness sets that guarantee correct results for specific ranges.
    
    Args:
        n: The number to test for primality
    
    Returns:
        True if n is prime, False if n is composite
    """
    # Handle small cases
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # For small numbers, use trial division for efficiency
    if n < 1000:
        return trial_division(n)
    
    # Write n-1 as d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Deterministic witness sets for different ranges
    # These are proven to be sufficient for their respective ranges
    if n < 2047:
        witnesses = [2]
    elif n < 1373653:
        witnesses = [2, 3]
    elif n < 9080191:
        witnesses = [31, 73]
    elif n < 25326001:
        witnesses = [2, 3, 5]
    elif n < 3215031751:
        witnesses = [2, 3, 5, 7]
    elif n < 4759123141:
        witnesses = [2, 7, 61]
    elif n < 1122004669633:
        witnesses = [2, 13, 23, 1662803]
    elif n < 2152302898747:
        witnesses = [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        witnesses = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        witnesses = [2, 3, 5, 7, 11, 13, 17]
    else:
        # For very large numbers, use probabilistic test with many rounds
        return miller_rabin(n, 40)
    
    # Test with deterministic witnesses
    for a in witnesses:
        if a >= n:
            continue
        
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

def trial_division(n):
    """
    Trial division primality test for small numbers.
    More efficient than Miller-Rabin for small inputs.
    
    Args:
        n: The number to test for primality
    
    Returns:
        True if n is prime, False if n is composite
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

def is_prime(n):
    """
    Main primality testing function that chooses the best algorithm.
    
    Args:
        n: The number to test for primality
    
    Returns:
        True if n is prime, False if n is composite
    """
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Quick check for small prime factors
    # This catches many composite numbers quickly
    small_primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    
    # Use deterministic Miller-Rabin for optimal performance
    return deterministic_miller_rabin(n)

# Additional utility functions for testing and validation

def generate_test_cases():
    """
    Generate test cases for validation (for development purposes).
    """
    test_cases = [
        (1, "NEITHER"),
        (2, "PRIME"),
        (3, "PRIME"),
        (4, "COMPOSITE"),
        (17, "PRIME"),
        (100, "COMPOSITE"),
        (561, "COMPOSITE"),  # Carmichael number
        (1105, "COMPOSITE"), # Carmichael number
        (999999999999999989, "PRIME"),  # Large prime
        (1000000007, "PRIME"),
        (1000000009, "PRIME"),
        (982451653, "PRIME"),
        (982451654, "COMPOSITE"),
    ]
    return test_cases

def validate_implementation():
    """
    Validate the implementation against known test cases.
    """
    test_cases = generate_test_cases()
    for n, expected in test_cases:
        if n == 1:
            result = "NEITHER"
        elif is_prime(n):
            result = "PRIME"
        else:
            result = "COMPOSITE"
        
        if result != expected:
            print(f"FAILED: {n} expected {expected}, got {result}")
            return False
        else:
            print(f"PASSED: {n} -> {result}")
    
    print("All test cases passed!")
    return True



"""
Efficient primality testing implementation using the Miller-Rabin algorithm.
Optimized for handling large numbers up to 10^18.
"""

import random

def miller_rabin(n, k=20):
    """
    Miller-Rabin probabilistic primality test.
    
    Args:
        n: The number to test for primality
        k: Number of rounds (witnesses) to test (default 20 for high accuracy)
    
    Returns:
        True if n is probably prime, False if n is definitely composite
    """
    # Handle small cases
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as d * 2^r by factoring out powers of 2
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        # Choose a random witness a in range [2, n-2]
        a = random.randrange(2, n - 1)
        
        # Compute a^d mod n
        x = pow(a, d, n)
        
        # If x is 1 or n-1, continue to next witness
        if x == 1 or x == n - 1:
            continue
        
        # Repeat r-1 times
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # If we never found n-1, n is composite
            return False
    
    # If all witnesses passed, n is probably prime
    return True

def deterministic_miller_rabin(n):
    """
    Deterministic Miller-Rabin test for numbers up to certain bounds.
    Uses known witness sets that guarantee correct results for specific ranges.
    
    Args:
        n: The number to test for primality
    
    Returns:
        True if n is prime, False if n is composite
    """
    # Handle small cases
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # For small numbers, use trial division for efficiency
    if n < 1000:
        return trial_division(n)
    
    # Write n-1 as d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Deterministic witness sets for different ranges
    # These are proven to be sufficient for their respective ranges
    if n < 2047:
        witnesses = [2]
    elif n < 1373653:
        witnesses = [2, 3]
    elif n < 9080191:
        witnesses = [31, 73]
    elif n < 25326001:
        witnesses = [2, 3, 5]
    elif n < 3215031751:
        witnesses = [2, 3, 5, 7]
    elif n < 4759123141:
        witnesses = [2, 7, 61]
    elif n < 1122004669633:
        witnesses = [2, 13, 23, 1662803]
    elif n < 2152302898747:
        witnesses = [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        witnesses = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        witnesses = [2, 3, 5, 7, 11, 13, 17]
    else:
        # For very large numbers, use probabilistic test with many rounds
        return miller_rabin(n, 40)
    
    # Test with deterministic witnesses
    for a in witnesses:
        if a >= n:
            continue
        
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

def trial_division(n):
    """
    Trial division primality test for small numbers.
    More efficient than Miller-Rabin for small inputs.
    
    Args:
        n: The number to test for primality
    
    Returns:
        True if n is prime, False if n is composite
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

def is_prime(n):
    """
    Main primality testing function that chooses the best algorithm.
    
    Args:
        n: The number to test for primality
    
    Returns:
        True if n is prime, False if n is composite
    """
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Quick check for small prime factors
    # This catches many composite numbers quickly
    small_primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    
    # Use deterministic Miller-Rabin for optimal performance
    return deterministic_miller_rabin(n)

# Additional utility functions for testing and validation

def generate_test_cases():
    """
    Generate test cases for validation (for development purposes).
    """
    test_cases = [
        (1, "NEITHER"),
        (2, "PRIME"),
        (3, "PRIME"),
        (4, "COMPOSITE"),
        (17, "PRIME"),
        (100, "COMPOSITE"),
        (561, "COMPOSITE"),  # Carmichael number
        (1105, "COMPOSITE"), # Carmichael number
        (999999999999999989, "PRIME"),  # Large prime
        (1000000007, "PRIME"),
        (1000000009, "PRIME"),
        (982451653, "PRIME"),
        (982451654, "COMPOSITE"),
    ]
    return test_cases

def validate_implementation():
    """
    Validate the implementation against known test cases.
    """
    test_cases = generate_test_cases()
    for n, expected in test_cases:
        if n == 1:
            result = "NEITHER"
        elif is_prime(n):
            result = "PRIME"
        else:
            result = "COMPOSITE"
        
        if result != expected:
            print(f"FAILED: {n} expected {expected}, got {result}")
            return False
        else:
            print(f"PASSED: {n} -> {result}")
    
    print("All test cases passed!")
    return True

if __name__ == "__main__":
    # Run validation if this module is executed directly
    validate_implementation()
