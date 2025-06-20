def miller_rabin_base(n, a):
    # Handle edge cases
    if n == 2 or n == a:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # Write n-1 as d * 2^r by factoring out powers of 2
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for _ in range(r - 1):
        x = (x * x) % n
        if x == n - 1:
            return True
        if x == 1:
            return False
    return False

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Miller-Rabin bases that are sufficient for numbers up to 2^64
    # This covers our range of 10^18
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in bases:
        if n == a:
            return True
        if not miller_rabin_base(n, a):
            return False
    return True

def main():
    try:
        # Read number of test cases
        T = int(input().strip())
        
        # Validate T is within constraints
        if not 1 <= T <= 100:
            print("Number of test cases must be between 1 and 100")
            return

        # Process each test case
        for _ in range(T):
            N = int(input().strip())
            
            # Validate N is within constraints
            if not 1 <= N <= 10**18:
                print("Number must be between 1 and 10^18")
                continue

            # Special case for 1
            if N == 1:
                print("NEITHER")
            # Check primality for all other numbers
            elif is_prime(N):
                print("PRIME")
            else:
                print("COMPOSITE")

    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
