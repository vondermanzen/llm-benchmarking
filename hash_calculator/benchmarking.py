import sys
import random
import string
import hashlib
import base64
from typing import List, Dict

def calculate_hash_chain(input_str: str) -> str:
    """Reference solution to calculate the hash chain."""
    try:
        # 1. Start with input string
        current = input_str
        
        # 2. Convert to UTF-8 bytes
        current = current.encode('utf-8')
        
        # 3. Calculate SHA-256 hash
        current = hashlib.sha256(current).digest()
        
        # 4. Convert to Base64
        current = base64.b64encode(current).decode('ascii')
        
        # 5. Calculate RIPEMD-160 hash
        current = hashlib.new('ripemd160', current.encode('utf-8')).digest()
        
        # 6. Convert to uppercase hex
        current = current.hex().upper()
        
        # 7. Calculate SHA-1 hash
        current = hashlib.sha1(current.encode('utf-8')).digest()
        
        # 8. Convert to lowercase hex
        current = current.hex().lower()
        
        # 9. Calculate SHA-512 hash
        current = hashlib.sha512(current.encode('utf-8')).digest()
        
        # 10. Take first 32 bytes
        current = current[:32]
        
        # 11. Calculate MD5 hash
        current = hashlib.md5(current).digest()
        
        # 12. Finally, calculate SHA-384 hash
        final_hash = hashlib.sha384(current).hexdigest()
        
        return final_hash
        
    except Exception as e:
        print(f"Error in reference solution: {str(e)}")
        return None

def generate_test_case(length: int = None, case_type: str = "random") -> str:
    """Generate a test case string."""
    if case_type == "special":
        # Special cases that might be tricky
        special_cases = [
            "",  # Empty string
            " ",  # Single space
            "a" * 1000,  # Maximum length string
            "!@#$%^&*()",  # Special characters
            "κόσμε",  # Unicode characters
            "\\n\\t\\r",  # Escape sequences
            "null",  # Common programming terms
            "0",  # Single digit
            "true",  # Boolean values
            "{\"key\": \"value\"}"  # JSON-like string
        ]
        return random.choice(special_cases)
    
    else:  # random
        if length is None:
            length = random.randint(1, 1000)
            
        # Mix of ASCII characters
        chars = string.ascii_letters + string.digits + string.punctuation + " "
        return ''.join(random.choice(chars) for _ in range(length))

def verify_solution(test_input: str, expected_output: str, received_output: str) -> bool:
    """Verify if the received output matches the expected output."""
    try:
        # Calculate correct hash
        correct_hash = calculate_hash_chain(test_input)
        
        # Clean and compare outputs
        received = received_output.strip().lower()
        expected = correct_hash.lower()
        
        return received == expected
        
    except:
        return False

def generate_test_cases() -> List[Dict]:
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example from prompt
    test_cases.append({
        "input": "Hello, World!",
        "output": None  # Will be computed
    })
    
    # Test case 2-6: Special cases
    for _ in range(5):
        test_cases.append({
            "input": generate_test_case(case_type="special"),
            "output": None
        })
    
    # Test case 7-10: Random cases of varying lengths
    lengths = [10, 50, 100, 1000]
    for length in lengths:
        test_cases.append({
            "input": generate_test_case(length=length),
            "output": None
        })
    
    # Compute expected outputs
    for case in test_cases:
        case["output"] = calculate_hash_chain(case["input"])
    
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
                thread.join(timeout=1)  # 1 second timeout
                
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
                    print(f"Input: {case['input'][:50]}...")
                    print(f"Expected: {case['output']}")
                    print(f"Received: {received_output.strip()}")
                
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