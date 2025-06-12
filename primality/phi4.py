def miller_rabin(n, k=5):  # number of tests = k
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Find r such that n = 2^d * r + 1
    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Witness loop
    import random
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        while d != n - 1:
            x = pow(x, 2, n)
            d *= 2
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

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        results.append(is_prime(N))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()