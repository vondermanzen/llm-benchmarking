import sys
import random
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

def generate_prime(bits: int) -> int:
    """Generate a prime number with the specified number of bits."""
    while True:
        # Generate random odd number
        n = random.getrandbits(bits) | 1
        if n.bit_length() != bits:
            continue
        if is_prime(n):
            return n

def generate_test_case(case_type: str = "random") -> Tuple[int, str]:
    """Generate a test case based on the type."""
    if case_type == "small_prime":
        return random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]), "PRIME"
        
    elif case_type == "large_prime":
        # Generate prime with 59-60 bits
        return generate_prime(random.randint(59, 60)), "PRIME"
        
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
        p = generate_prime(30)
        q = generate_prime(30)
        return p * q, "COMPOSITE"
        
    else:  # random
        n = random.randint(1, 10**18)
        if n == 1:
            return n, "NEITHER"
        return n, "PRIME" if is_prime(n) else "COMPOSITE"

def verify_solution(test_input: str, expected_output: str, received_output: str) -> bool:
    """Verify if the received output matches the expected output."""
    try:
        # Parse input
        lines = test_input.strip().split("\n")
        T = int(lines[0])
        numbers = [int(lines[i]) for i in range(1, T + 1)]
        
        # Parse output
        received_lines = received_output.strip().split("\n")
        if len(received_lines) != T:
            return False
            
        # Verify each test case
        for i, n in enumerate(numbers):
            received = received_lines[i].strip()
            if n == 1:
                if received != "NEITHER":
                    return False
            else:
                is_n_prime = is_prime(n)
                if is_n_prime and received != "PRIME":
                    return False
                if not is_n_prime and received != "COMPOSITE":
                    return False
        
        return True
        
    except:
        return False

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

def run_tests(solution_file: str) -> None:
    """Run all test cases and score the solution."""
    try:
        with open(solution_file, 'r') as f:
            solution_code = f.read()
        
        # Create a temporary module to run the solution
        import importlib.util
        spec = importlib.util.spec_from_file_location("solution", solution_file)
        solution = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(solution)
        
        test_cases = generate_test_cases()
        total_score = 0
        max_score = len(test_cases)
        
        for i, case in enumerate(test_cases, 1):
            try:
                # Redirect stdin to provide input
                import io
                import sys
                sys.stdin = io.StringIO(case["input"])
                
                # Capture stdout
                from io import StringIO
                captured_output = StringIO()
                sys.stdout = captured_output
                
                # Run solution with timeout
                import threading
                import _thread
                def run_solution():
                    solution.main()
                
                thread = threading.Thread(target=run_solution)
                thread.start()
                thread.join(timeout=2)  # 2 second timeout
                
                if thread.is_alive():
                    _thread.interrupt_main()
                    raise TimeoutError("Solution took too long")
                
                received_output = captured_output.getvalue()
                
                # Verify output
                if verify_solution(case["input"], case["output"], received_output):
                    total_score += 1
                    print(f"Test case {i}: Passed")
                else:
                    print(f"Test case {i}: Failed")
                    print(f"Input:")
                    print(case["input"])
                    print(f"Expected:")
                    print(case["output"])
                    print(f"Received:")
                    print(received_output.strip())
                
            except Exception as e:
                print(f"Test case {i}: Error - {str(e)}")
            
            finally:
                # Reset stdin and stdout
                sys.stdin = sys.__stdin__
                sys.stdout = sys.__stdout__
        
        # Calculate and print final score
        final_score = (total_score / max_score) * 100
        print(f"\nFinal Score: {final_score:.2f}%")
        print(f"Passed {total_score} out of {max_score} test cases")
        
    except Exception as e:
        print(f"Error running tests: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python benchmarking.py <solution_file>")
        sys.exit(1)
    
    run_tests(sys.argv[1]) 