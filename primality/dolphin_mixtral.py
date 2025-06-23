import random

def is_prime(n, k=5):
    if n == 1:
        return "NEITHER"
    elif n == 2 or n == 3:
        return "PRIME"
    elif n % 2 == 0:
        return "COMPOSITE"
    else:
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return "COMPOSITE"
        return "PRIME"

t = int(input())
for _ in range(t):
    n = int(input())
    print(is_prime(n))