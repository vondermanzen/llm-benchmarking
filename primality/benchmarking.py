import sys
import random
import subprocess
import os
from typing import List, Dict, Tuple

def miller_rabin_base(n: int, a: int) -> bool:
    """
    Miller-Rabin primality test for a single base a.
    Returns False if n is definitely composite, True if possibly prime.
    """
    if n == a:
        return True
    if n % 2 == 0:
        return False
        
    # Write n-1 as d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
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

def is_prime(n: int) -> bool:
    """
    Deterministic Miller-Rabin primality test.
    Implementation uses verified small bases that work up to 2^64.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
        
    # For n < 2^64, it is enough to test these bases
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    for a in bases:
        if n == a:
            return True
        if n > a and not miller_rabin_base(n, a):
            return False
    return True

def generate_test_case(case_type: str = "random") -> Tuple[int, str]:
    """Generate a test case based on the type."""
    if case_type == "small_prime":
        # Small primes under 10^6
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                       997, 1009, 9973, 99991, 999983]
        return random.choice(small_primes), "PRIME"
        
    elif case_type == "large_prime":
        # Generate prime near 10^18
        # Start with a number close to 10^18 and search for next prime
        start = random.randint(10**17, 10**18)
        if start % 2 == 0:
            start += 1
        n = start
        while not is_prime(n) and n < 10**18:
            n += 2
        if not is_prime(n):  # If we hit 10^18, try going down
            n = start
            while not is_prime(n) and n > 10**17:
                n -= 2
        return n, "PRIME"
        
    elif case_type == "carmichael":
        # Expanded list of Carmichael numbers
        carmichael = [
            561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341,
            41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921,
            126217, 162401, 172081, 188461, 252601, 278545, 294409,
            314821, 334153, 340561, 399001, 410041, 449065, 488881
        ]
        return random.choice(carmichael), "COMPOSITE"
        
    elif case_type == "perfect_power":
        # Generate perfect square, cube, or fourth power
        base = random.randint(2, int(10**4.5))  # Up to ~10^18 when cubed
        power = random.randint(2, 4)
        return base ** power, "COMPOSITE"
        
    elif case_type == "small_factors":
        # Generate number with small prime factors but large result
        small_prime = random.choice([2, 3, 5, 7, 11, 13, 17, 19])
        # Make sure product is large but under 10^18
        max_factor = int(10**18 / small_prime)
        large_factor = random.randint(max_factor // 100, max_factor)
        return small_prime * large_factor, "COMPOSITE"
        
    elif case_type == "large_semiprimes":
        # Product of two large primes near sqrt(10^18)
        def generate_prime_near(target):
            n = target + random.randint(-1000, 1000)
            if n % 2 == 0:
                n += 1
            while not is_prime(n):
                n += 2
            return n
        
        # Generate two primes near sqrt(10^18) ≈ 10^9
        p = generate_prime_near(10**9)
        q = generate_prime_near(10**9)
        return p * q, "COMPOSITE"
        
    else:  # random
        # Generate random numbers across the full range
        n = random.randint(1, 10**18)
        if n == 1:
            return n, "NEITHER"
        return n, "PRIME" if is_prime(n) else "COMPOSITE"

def generate_test_cases() -> List[Dict]:
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example from prompt
    test_cases.append({
        "input": "5\n2\n17\n1\n100\n999999999999999989",
        "output": "PRIME\nPRIME\nNEITHER\nCOMPOSITE\nPRIME"
    })
    
    # Test case 2: Small numbers and edge cases
    cases = [
        (1, "NEITHER"),
        (2, "PRIME"),
        generate_test_case("small_prime"),
        (4, "COMPOSITE"),
        generate_test_case("perfect_power")
    ]
    test_cases.append({
        "input": f"{len(cases)}\n" + "\n".join(str(n) for n, _ in cases),
        "output": "\n".join(result for _, result in cases)
    })
    
    # Test case 3: Carmichael and special composites
    cases = [
        generate_test_case("carmichael"),
        generate_test_case("perfect_power"),
        generate_test_case("small_factors"),
        generate_test_case("large_semiprimes"),
        generate_test_case("carmichael")  # Another Carmichael number
    ]
    test_cases.append({
        "input": f"{len(cases)}\n" + "\n".join(str(n) for n, _ in cases),
        "output": "\n".join(result for _, result in cases)
    })
    
    # Test case 4: Large numbers
    cases = [
        generate_test_case("large_prime"),
        generate_test_case("large_semiprimes"),
        generate_test_case("large_prime"),
        generate_test_case("small_factors"),
        generate_test_case("large_prime")
    ]
    test_cases.append({
        "input": f"{len(cases)}\n" + "\n".join(str(n) for n, _ in cases),
        "output": "\n".join(result for _, result in cases)
    })
    
    # Test case 5: Mixed random cases
    cases = [generate_test_case() for _ in range(5)]
    test_cases.append({
        "input": f"{len(cases)}\n" + "\n".join(str(n) for n, _ in cases),
        "output": "\n".join(result for _, result in cases)
    })
    
    return test_cases

# Current benchmarking script's filename
benchmark_file = 'benchmarking.py'

# List all .py files in the current directory except this one
py_files = [f for f in os.listdir('.') if f.endswith('.py') and f != benchmark_file]

results = {}

# Generate test cases once to use for all solutions
test_cases = generate_test_cases()

for file in py_files:
    correct = 0
    total = len(test_cases)
    
    for case in test_cases:
        try:
            # Run the script with input and capture output
            result = subprocess.run(
                ['python', file],
                input=case["input"].encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=2  # 2 second timeout per test case
            )
            output = result.stdout.decode().strip()
            if output == case["output"]:
                correct += 1
            
        except Exception as e:
            pass  # Failed test case
    
    results[file] = f"{correct}/{total}"

# Print summary of results
print("\nScript Evaluation Results:")
print("-" * 30)
for script, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"{script}: {score}") 