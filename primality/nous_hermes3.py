import random

def is_prime(n, k=5):
    if n == 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print("NEITHER")
    elif is_prime(n):
        print("PRIME")
    else:
        print("COMPOSITE")