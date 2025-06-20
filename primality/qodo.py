import sys

def is_prime(n):
    if n == 1:
        return "NEITHER"
    if n == 2 or n == 3:
        return "PRIME"
    if n % 2 == 0:
        return "COMPOSITE"
    # Miller-Rabin deterministic bases for n < 2^64
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in bases:
        if a >= n:
            continue
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
    input_lines = sys.stdin.read().splitlines()
    T = int(input_lines[0])
    for i in range(1, T + 1):
        N = int(input_lines[i])
        print(is_prime(N))

if __name__ == "__main__":
    main()