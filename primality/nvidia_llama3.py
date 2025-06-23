import random

def miller_rabin(n, k=5):
    if n < 2:
        return "NEITHER"
    if n == 2 or n == 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        if not check(a, s, d, n):
            return "COMPOSITE"
    return "PRIME"

T = int(input())
for _ in range(T):
    N = int(input())
    print(miller_rabin(N))