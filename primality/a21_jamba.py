import random

def miller_rabin_test(n, k=50):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    def is_composite(a, s, d, n):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True

    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        if is_composite(a, s, d, n):
            return False

    return True

def is_prime(n):
    if n == 1:
        return "NEITHER"
    if miller_rabin_test(n):
        return "PRIME"
    return "COMPOSITE"

def main():
    T = int(input())
    results = []
    for _ in range(T):
        N = int(input())
        results.append(is_prime(N))
    print("\n".join(results))

if __name__ == "__main__":
    main()