import random

def is_prime(n, k=5):  # k is the number of Miller-Rabin iterations
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # write n as 2^r * d + 1 with d odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # perform k iterations of Miller-Rabin
    for _ in range(k):
        a = random.randrange(2, n - 1)
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

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print("NEITHER")
    elif is_prime(N):
        print("PRIME")
    else:
        print("COMPOSITE")