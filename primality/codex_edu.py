import sys

# Deterministic Miller-Rabin primality test for 64-bit numbers

_SMALL_PRIMES = [2, 3, 5, 7, 11, 13]
_MR_BASES = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]


def _is_strong_probable_prime(n, a, d, s):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in _SMALL_PRIMES:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in _MR_BASES:
        if a % n == 0:
            return True
        if not _is_strong_probable_prime(n, a, d, s):
            return False
    return True


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        n = int(data[i])
        if n == 1:
            results.append("NEITHER")
        elif is_prime(n):
            results.append("PRIME")
        else:
            results.append("COMPOSITE")
    print("\n".join(results))


if __name__ == "__main__":
    main()
