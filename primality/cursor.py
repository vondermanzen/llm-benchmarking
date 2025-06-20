import sys
import random

def is_prime(n, k=10):
    if n == 1:
        return "NEITHER"
    if n == 2 or n == 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"
    # Write n-1 as 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    # Miller-Rabin test
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
            return "COMPOSITE"
    return "PRIME"

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(is_prime(N))
