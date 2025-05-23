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
        return "", calculate_hash("")
        
    elif case_type == "single_char":
        # Single character
        char = random.choice(string.ascii_letters)
        return char, calculate_hash(char)
        
    elif case_type == "special_chars":
        # String with special characters
        chars = string.punctuation
        length = random.randint(5, 20)
        text = ''.join(random.choice(chars) for _ in range(length))
        return text, calculate_hash(text)
        
    elif case_type == "long_string":
        # Long string
        chars = string.ascii_letters + string.digits + string.punctuation + ' '
        length = random.randint(1000, 2000)
        text = ''.join(random.choice(chars) for _ in range(length))
        return text, calculate_hash(text)
        
    else:  # random
        # Random string of random length
        chars = string.ascii_letters + string.digits + ' '
        length = random.randint(10, 100)
        text = ''.join(random.choice(chars) for _ in range(length))
        return text, calculate_hash(text)

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
    
    # Test case 1: Example case
    test_cases.append({
        "input": "1\nHello, World!",
        "output": "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"
    })
    
    # Test case 2: Multiple test cases with different types
    cases = [
        generate_test_case("empty"),
        generate_test_case("single_char"),
        generate_test_case("special_chars"),
        generate_test_case("long_string"),
        generate_test_case("random")
    ]
    combined_input = str(len(cases)) + "\n" + "\n".join(input_str for input_str, _ in cases)
    combined_output = "\n".join(output for _, output in cases)
    test_cases.append({
        "input": combined_input,
        "output": combined_output
    })
    
    # Test case 3: Large random cases
    random_cases = [generate_test_case("random") for _ in range(5)]
    combined_input = str(len(random_cases)) + "\n" + "\n".join(input_str for input_str, _ in random_cases)
    combined_output = "\n".join(output for _, output in random_cases)
    test_cases.append({
        "input": combined_input,
        "output": combined_output
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

