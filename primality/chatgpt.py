def is_prime(n):
    if n == 1:
        return "NEITHER"
    if n == 2 or n == 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"

    # Write n-1 as 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Deterministic Miller-Rabin test for n < 2^64
    # These bases are sufficient to guarantee correctness for n < 3.3e18
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    def try_composite(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True  # Composite

    for base in bases:
        if base >= n:
            continue
        if try_composite(base):
            return "COMPOSITE"
    return "PRIME"

# Reading input
T = int(input())
for _ in range(T):
    N = int(input())
    print(is_prime(N))
