import sys
import random
import string
import hashlib
import base64
import subprocess
import os
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

def calculate_hash(text: str) -> str:
    """Reference implementation for calculating hash."""
    return hashlib.sha256(text.encode()).hexdigest()

def generate_test_case(case_type: str = "random") -> Tuple[str, str]:
    """Generate a test case based on the type."""
    if case_type == "empty":
        # Empty string
        return "", calculate_hash_chain("")
        
    elif case_type == "single_char":
        # Single character
        char = random.choice(string.ascii_letters)
        return char, calculate_hash_chain(char)
        
    elif case_type == "special_chars":
        # String with special characters
        chars = string.punctuation
        length = random.randint(5, 20)
        text = ''.join(random.choice(chars) for _ in range(length))
        return text, calculate_hash_chain(text)
        
    elif case_type == "long_string":
        # Long string
        chars = string.ascii_letters + string.digits + string.punctuation + ' '
        length = random.randint(500, 1000)  # Max length 1000 per prompt
        text = ''.join(random.choice(chars) for _ in range(length))
        return text, calculate_hash_chain(text)
        
    else:  # random
        # Random string of random length
        chars = string.ascii_letters + string.digits + ' '
        length = random.randint(10, 100)
        text = ''.join(random.choice(chars) for _ in range(length))
        return text, calculate_hash_chain(text)

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
        "output": "a9842d666c6d9a334d8987a0628c68d5302e9251c7e9f0168f7b5dd2b7ff2763c9ae92b6e4c574e4ba05c3108468db17"
    })
    
    # Test case 2: Different types of strings
    cases = [
        generate_test_case("empty"),
        generate_test_case("single_char"),
        generate_test_case("special_chars"),
        generate_test_case("long_string"),
        generate_test_case("random")
    ]
    
    # Add each case individually
    for input_str, output in cases:
        test_cases.append({
            "input": input_str,
            "output": output
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

