def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n == 1:
            print("NEITHER")
        elif n == 2:
            print("PRIME")
        else:
            if is_prime(n):
                print("PRIME")
            else:
                print("COMPOSITE")

if __name__ == "__main__":
    main()