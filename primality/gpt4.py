import random

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def miller_rabin_test(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
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

def is_prime(n, k=5):
    if n == 1:
        return "NEITHER"
    if n == 2 or n == 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        if not miller_rabin_test(s, n):
            return "COMPOSITE"
    return "PRIME"

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(is_prime(N))