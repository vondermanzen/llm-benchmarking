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
        return random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]), "PRIME"
        
    elif case_type == "large_prime":
        # Generate prime with 59-60 bits
        n = random.getrandbits(random.randint(59, 60)) | 1
        while not is_prime(n):
            n = random.getrandbits(random.randint(59, 60)) | 1
        return n, "PRIME"
        
    elif case_type == "carmichael":
        # Some small Carmichael numbers
        carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341]
        return random.choice(carmichael), "COMPOSITE"
        
    elif case_type == "perfect_power":
        # Generate perfect square or cube
        base = random.randint(2, 1000)
        power = random.randint(2, 3)
        return base ** power, "COMPOSITE"
        
    elif case_type == "small_factors":
        # Generate number with small prime factors
        p = random.choice([2, 3, 5, 7, 11, 13, 17, 19])
        q = random.randint(1000, 10000)
        return p * q, "COMPOSITE"
        
    elif case_type == "large_semiprimes":
        # Product of two large primes
        p = random.getrandbits(30) | 1
        while not is_prime(p):
            p = random.getrandbits(30) | 1
        q = random.getrandbits(30) | 1
        while not is_prime(q):
            q = random.getrandbits(30) | 1
        return p * q, "COMPOSITE"
        
    else:  # random
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
    
    # Test case 2: Small numbers
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    outputs = ["PRIME" if is_prime(n) else "COMPOSITE" for n in numbers]
    test_cases.append({
        "input": f"{len(numbers)}\n" + "\n".join(map(str, numbers)),
        "output": "\n".join(outputs)
    })
    
    # Test case 3: Special cases
    cases = [
        (1, "NEITHER"),
        generate_test_case("carmichael"),
        generate_test_case("perfect_power"),
        generate_test_case("small_factors"),
        generate_test_case("large_semiprimes")
    ]
    test_cases.append({
        "input": f"{len(cases)}\n" + "\n".join(str(n) for n, _ in cases),
        "output": "\n".join(result for _, result in cases)
    })
    
    # Test case 4: Large primes
    large_cases = [generate_test_case("large_prime") for _ in range(5)]
    test_cases.append({
        "input": f"{len(large_cases)}\n" + "\n".join(str(n) for n, _ in large_cases),
        "output": "\n".join(result for _, result in large_cases)
    })
    
    # Test case 5: Mixed random cases
    random_cases = [generate_test_case() for _ in range(10)]
    test_cases.append({
        "input": f"{len(random_cases)}\n" + "\n".join(str(n) for n, _ in random_cases),
        "output": "\n".join(result for _, result in random_cases)
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