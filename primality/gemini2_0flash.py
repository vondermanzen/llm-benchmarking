import random

def power(a, d, n):
    res = 1
    a = a % n
    while d > 0:
        if d % 2 == 1:
            res = (res * a) % n
        a = (a * a) % n
        d //= 2
    return res

def miller_rabin(n, k=5):
    if n <= 1:
        return "NEITHER"
    if n <= 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                break
        else:
            return "COMPOSITE"
    return "PRIME"

T = int(input())
for _ in range(T):
    N = int(input())
    print(miller_rabin(N))