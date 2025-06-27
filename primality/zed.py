import random


def miller_rabin(n, k=20):
    """
    Miller-Rabin probabilistic primality test.

    Args:
        n: Number to test for primality
        k: Number of rounds (higher k = more accurate)

    Returns:
        True if n is probably prime, False if n is composite
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

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d mod n

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def deterministic_miller_rabin(n):
    """
    Deterministic Miller-Rabin for numbers up to certain bounds.
    Uses specific witness sets that guarantee correctness.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Small primes check
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    # Write n-1 as d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Deterministic witnesses for different ranges
    if n < 341550071728321:
        witnesses = [2, 3, 5, 7, 11, 13, 17]
    else:
        # For very large numbers, use more witnesses
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

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


def is_prime(n):
    """
    Main primality test function.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # For smaller numbers, use trial division for speed
    if n < 1000000:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    # For larger numbers, use deterministic Miller-Rabin
    return deterministic_miller_rabin(n)


def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        if n == 1:
            print("NEITHER")
        elif is_prime(n):
            print("PRIME")
        else:
            print("COMPOSITE")


if __name__ == "__main__":
    main()

