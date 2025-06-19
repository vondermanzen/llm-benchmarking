import random

def is_prime(n):
    if n == 1:
        return "NEITHER"
    if n == 2 or n == 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"

    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(5):  # Number of iterations for higher accuracy
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return "COMPOSITE"
    return "PRIME"

T = int(input())
for _ in range(T):
    N = int(input())
    print(is_prime(N))