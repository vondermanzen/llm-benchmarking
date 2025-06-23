import sys
import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    input_lines = sys.stdin.read().split()
    T = int(input_lines[0])
    for i in range(1, T + 1):
        N = int(input_lines[i])
        if N == 1:
            print("NEITHER")
        else:
            if is_prime(N):
                print("PRIME")
            else:
                print("COMPOSITE")

if __name__ == "__main__":
    main()