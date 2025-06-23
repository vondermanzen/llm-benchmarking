def is_prime(n):
    if n == 1:
        return "NEITHER"
    if n < 4:
        return "PRIME"  # 2 and 3 are prime
    if n % 2 == 0:
        return "COMPOSITE"
    if n < 9:
        return "PRIME"  # 5 and 7 are prime
    if n % 3 == 0:
        return "COMPOSITE"

    # Miller-Rabin primality test implementation
    def miller_rabin_test(d, n, a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    def is_miller_rabin_prime(n):
        # Write n-1 as d * 2^r
        d = n - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1

        # Deterministic bases for testing primality for 64-bit integers
        # According to research, testing these bases is enough for 64-bit numbers:
        # 2, 325, 9375, 28178, 450775, 9780504, 1795265022
        # This covers all n < 2^64, and our max is 10^18 < 2^60, so safe.
        test_bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

        for a in test_bases:
            if a % n == 0:
                return True
            if not miller_rabin_test(d, n, a):
                return False
        return True

    return "PRIME" if is_miller_rabin_prime(n) else "COMPOSITE"


T = int(input())
for _ in range(T):
    N = int(input())
    print(is_prime(N))