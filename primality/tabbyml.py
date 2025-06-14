def is_prime(n):
    if n <= 1:
        return "COMPOSITE"
    if n == 2:
        return "PRIME"
    if n % 2 == 0:
        return "NEITHER"
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return "COMPOSITE"
    return "PRIME"

T = int(input())
for _ in range(T):
    n = int(input())
    print(is_prime(n))