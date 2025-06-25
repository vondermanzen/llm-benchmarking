import sys
import random

# Fast Miller-Rabin primality test

def is_probable_prime(n, k=10):
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False

    # write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = random.randrange(2, min(n - 2, sys.maxsize))
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

# Read input
T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print("NEITHER")
    elif is_probable_prime(N):
        print("PRIME")
    else:
        print("COMPOSITE")
