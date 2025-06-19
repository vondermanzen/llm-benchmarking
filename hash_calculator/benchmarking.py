import sys
import subprocess
import os
import hashlib
import base64
import time
from typing import List, Dict, Tuple

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
        current = base64.b64encode(current)
        
        # 5. Calculate RIPEMD-160 hash
        current = hashlib.new('ripemd160', current).digest()
        
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

def verify_solution(test_input: str, expected_output: str, received_output: str) -> bool:
    """Verify if the received output matches the expected output."""
    try:
        # Clean and compare outputs
        received = received_output.strip().lower()
        expected = expected_output.lower()
        
        return received == expected
        
    except:
        return False

def generate_test_cases() -> List[Dict]:
    """Generate hardcoded test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example from prompt
    test_cases.append({
        "input": "Hello, World!",
        "output": calculate_hash_chain("Hello, World!"),
        "description": "Example from prompt - standard greeting string"
    })
    
    # Test case 2: Empty string
    test_cases.append({
        "input": "\n",
        "output": calculate_hash_chain(""),
        "description": "Empty string - edge case"
    })
    
    # Test case 3: Single character
    test_cases.append({
        "input": "a",
        "output": calculate_hash_chain("a"),
        "description": "Single lowercase letter"
    })
    
    # Test case 4: Single uppercase character
    test_cases.append({
        "input": "A",
        "output": calculate_hash_chain("A"),
        "description": "Single uppercase letter"
    })
    
    # Test case 5: Numbers only
    test_cases.append({
        "input": "123456789",
        "output": calculate_hash_chain("123456789"),
        "description": "Numeric string - digits only"
    })
    
    # Test case 6: Special characters
    test_cases.append({
        "input": "!@#$%^&*()",
        "output": calculate_hash_chain("!@#$%^&*()"),
        "description": "Special characters - symbols and punctuation"
    })
    
    # Test case 7: Mixed case with spaces
    test_cases.append({
        "input": "The Quick Brown Fox",
        "output": calculate_hash_chain("The Quick Brown Fox"),
        "description": "Mixed case letters with spaces"
    })

    
    # Test case 8: JSON-like string
    test_cases.append({
        "input": '{"key": "value", "number": 42}',
        "output": calculate_hash_chain('{"key": "value", "number": 42}'),
        "description": "JSON-like string with quotes and braces"
    })
    
    # Test case 9: Long string with repeating pattern
    test_cases.append({
        "input": "abcdefghijklmnopqrstuvwxyz" * 10,
        "output": calculate_hash_chain("abcdefghijklmnopqrstuvwxyz" * 10),
        "description": "Long string - 260 characters of repeating alphabet"
    })
    
    # Test case 10: Base64-like string
    test_cases.append({
        "input": "SGVsbG8gV29ybGQ=",
        "output": calculate_hash_chain("SGVsbG8gV29ybGQ="),
        "description": "Base64-like string with padding"
    })
    
    # Test case 11: Programming code snippet  
    test_cases.append({
        "input": "def hello(): print('Hello!')",
        "output": calculate_hash_chain("def hello(): print('Hello!')"),
        "description": "Python code snippet without newlines"
    })
    
    # Test case 12: SQL injection attempt
    test_cases.append({
        "input": "'; DROP TABLE users; --",
        "output": calculate_hash_chain("'; DROP TABLE users; --"),
        "description": "SQL injection string - security testing"
    })
    
    # Test case 13: XML/HTML tags
    test_cases.append({
        "input": "<html><body>Test</body></html>",
        "output": calculate_hash_chain("<html><body>Test</body></html>"),
        "description": "HTML/XML tags with angle brackets"
    })
    
    # Test case 14: Long single character repetition
    test_cases.append({
        "input": "x" * 500,
        "output": calculate_hash_chain("x" * 500),
        "description": "Long string - 500 repeated characters"
    })
    
    return test_cases

# Current benchmarking script's filename
benchmark_file = 'benchmarking.py'

# List all .py files in the current directory except this one
py_files = [f for f in os.listdir('.') if f.endswith('.py') and f != benchmark_file]

results = {}
detailed_results = {}

# Generate test cases once to use for all solutions
test_cases = generate_test_cases()

for file in py_files:
    correct = 0
    total = len(test_cases)
    failed_cases = []
    total_time = 0
    any_failed = False
    
    for i, case in enumerate(test_cases):
        try:
            # Run the script with input and capture output
            start_time = time.time()
            result = subprocess.run(
                ['python', file],
                input=case["input"].encode('utf-8'),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=2  # 2 second timeout per test case
            )
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            output = result.stdout.decode().strip()
            if verify_solution(case["input"], case["output"], output):
                correct += 1
            # Add time for all test cases, not just correct ones
            total_time += execution_time
            if not verify_solution(case["input"], case["output"], output):
                failed_cases.append({
                    'case_num': i + 1,
                    'description': case.get('description', f'Test case {i + 1}'),
                    'input': case["input"][:100] + "..." if len(case["input"]) > 100 else case["input"],
                    'expected': case["output"],
                    'actual': output,
                    'stderr': result.stderr.decode().strip() if result.stderr else None
                })
            
        except Exception as e:
            any_failed = True
            failed_cases.append({
                'case_num': i + 1,
                'description': case.get('description', f'Test case {i + 1}'),
                'input': case["input"][:100] + "..." if len(case["input"]) > 100 else case["input"],
                'expected': case["output"],
                'actual': 'ERROR',
                'error': str(e)
            })
    
    # If any test case failed to execute, set total time to infinity
    if any_failed:
        total_time = float('inf')
    
    # Use total time for all test cases
    results[file] = {
        'score': f"{correct}/{total}",
        'total_time_ms': round(total_time, 2) if total_time != float('inf') else float('inf')
    }
    detailed_results[file] = failed_cases

# Print summary of results
print("Script Evaluation Results:")
print("-" * 50)
print(f"{'Script':<20} {'Score':<10} {'Total Time (ms)':<15}")
print("-" * 50)
for script, result in sorted(results.items(), key=lambda x: (x[1]['score'], -x[1]['total_time_ms']), reverse=True):
    print(f"{script:<20} {result['score']:<10} {result['total_time_ms']:<15.2f}")

# Only show detailed failure analysis if not called from parent script
show_details = True
if len(sys.argv) > 1 and sys.argv[1] == "--no-details":
    show_details = False
elif os.path.basename(os.getcwd()) != os.path.basename(os.path.dirname(__file__)):
    # If current working directory is not the script's directory, likely called from parent
    show_details = False

if show_details:
    # Print detailed failure information
    print("\nDetailed Failure Analysis:")
    print("=" * 50)
    for script in sorted(py_files):
        score = results[script]['score']
        if detailed_results[script]:
            print(f"\n{script} - {score} - Failed Cases:")
            print("-" * 30)
            for failure in detailed_results[script]:
                print(f"Test Case {failure['case_num']}: {failure['description']}")
                print(f"Input: {failure['input']}")
                print(f"Expected: {failure['expected']}")
                print(f"Actual: {failure['actual']}")
                if 'error' in failure:
                    print(f"Error: {failure['error']}")
                if failure.get('stderr'):
                    print(f"Stderr: {failure['stderr']}")
                print()
        else:
            print(f"\n{script}: {score}")

