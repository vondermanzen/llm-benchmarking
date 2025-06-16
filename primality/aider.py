import sys
import random

def is_prime(n, k=5):  # number of tests
    if n <= 1:
        return "NEITHER"
    if n <= 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"
    
    # Write n as d*2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return "COMPOSITE"
    return "PRIME"

def main():
    input = sys.stdin.read
    data = input().splitlines()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        results.append(is_prime(N))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
