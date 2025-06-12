import random

def miller_rabin(n, k=10):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
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
            return False
    return True

def is_prime(n):
    if n == 1:
        return "NEITHER"
    if miller_rabin(n):
        return "PRIME"
    return "COMPOSITE"

t = int(input())
for _ in range(t):
    n = int(input())
    print(is_prime(n))