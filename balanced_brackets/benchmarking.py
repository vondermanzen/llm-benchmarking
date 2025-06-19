import sys
import subprocess
import os
import time
from typing import List, Dict, Optional, Tuple

def is_balanced(s: str) -> bool:
    """Reference implementation to check if brackets are balanced."""
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0

def generate_test_cases() -> List[Dict]:
    """Generate hardcoded test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example from prompt - balanced
    test_cases.append({
        "input": "6\n{[()]}",
        "output": "YES",
        "description": "Example from prompt - properly nested mixed brackets"
    })
    
    # Test case 2: Example from prompt - unbalanced (wrong order)
    test_cases.append({
        "input": "4\n{[}]",
        "output": "NO",
        "description": "Example from prompt - brackets closed in wrong order"
    })
    
    # Test case 3: Example from prompt - unbalanced (wrong bracket)
    test_cases.append({
        "input": "2\n)(",
        "output": "NO",
        "description": "Example from prompt - closing bracket before opening"
    })
    
    # Test case 4: Empty string
    test_cases.append({
        "input": "0\n\n",
        "output": "YES",
        "description": "Empty string - trivially balanced"
    })
    
    # Test case 5: Single opening bracket
    test_cases.append({
        "input": "1\n(",
        "output": "NO",
        "description": "Single opening bracket - unbalanced"
    })
    
    # Test case 6: Single closing bracket
    test_cases.append({
        "input": "1\n)",
        "output": "NO",
        "description": "Single closing bracket - unbalanced"
    })
    
    # Test case 7: Simple balanced pair
    test_cases.append({
        "input": "2\n()",
        "output": "YES",
        "description": "Simple balanced parentheses"
    })
    
    # Test case 8: Multiple same type brackets
    test_cases.append({
        "input": "6\n((()))",
        "output": "YES",
        "description": "Nested parentheses - all same type"
    })
    
    # Test case 9: All three bracket types
    test_cases.append({
        "input": "6\n(){}[]",
        "output": "YES",
        "description": "All three bracket types in sequence"
    })
    
    # Test case 10: Complex nested structure
    test_cases.append({
        "input": "12\n{[()]}[(){}]",
        "output": "YES",
        "description": "Complex nested structure with multiple groups"
    })
    
    # Test case 11: Wrong closing bracket type
    test_cases.append({
        "input": "4\n(]",
        "output": "NO",
        "description": "Wrong closing bracket type - parenthesis opened, bracket closed"
    })
    
    # Test case 12: Extra closing bracket
    test_cases.append({
        "input": "5\n(()))",
        "output": "NO",
        "description": "Extra closing bracket - one too many"
    })
    
    # Test case 13: Missing closing bracket
    test_cases.append({
        "input": "5\n((()",
        "output": "NO",
        "description": "Missing closing bracket - not enough closing"
    })
    
    # Test case 14: Interleaved brackets (valid)
    test_cases.append({
        "input": "8\n([{}])",
        "output": "YES",
        "description": "Properly interleaved different bracket types"
    })
    
    # Test case 15: Interleaved brackets (invalid)
    test_cases.append({
        "input": "6\n([)]",
        "output": "NO",
        "description": "Improperly interleaved brackets - crossing structure"
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
                input=case["input"].encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=2  # 2 second timeout per test case
            )
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            output = result.stdout.decode().strip()
            if output == case["output"]:
                correct += 1
            # Add time for all test cases, not just correct ones
            total_time += execution_time
            if output != case["output"]:
                failed_cases.append({
                    'case_num': i + 1,
                    'description': case.get('description', f'Test case {i + 1}'),
                    'input': case["input"],
                    'expected': case["output"],
                    'actual': output,
                    'stderr': result.stderr.decode().strip() if result.stderr else None
                })
            
        except Exception as e:
            any_failed = True
            failed_cases.append({
                'case_num': i + 1,
                'description': case.get('description', f'Test case {i + 1}'),
                'input': case["input"],
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
                print(f"Input:\n{failure['input']}")
                print(f"Expected: {failure['expected']}")
                print(f"Actual: {failure['actual']}")
                if 'error' in failure:
                    print(f"Error: {failure['error']}")
                if failure.get('stderr'):
                    print(f"Stderr: {failure['stderr']}")
                print()
        else:
            print(f"\n{script}: {score}") 