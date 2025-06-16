def is_prime_miller_rabin(n, k=40):
    """Miller-Rabin primality test"""
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = pow(2 + _ % (n - 4), 1, n)  # Using deterministic witnesses for n < 3,317,044,064,679,887,385,961,981
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

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 1:
            print("NEITHER")
        elif is_prime_miller_rabin(n):
            print("PRIME")
        else:
            print("COMPOSITE")

if __name__ == "__main__":
    main()