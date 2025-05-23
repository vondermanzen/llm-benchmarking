import sys
import random
import subprocess
import os
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

def generate_test_case(case_type: str = "random") -> Tuple[str, str]:
    """Generate a test case based on the type."""
    if case_type == "always_balanced":
        # Generate perfectly balanced brackets
        n = random.randint(3, 10)
        brackets = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        stack = []
        
        for i in range(n * 2):
            if i < n:  # First half: mostly opening brackets
                bracket_type = random.randint(0, 2)
                brackets.append(opening[bracket_type])
                stack.append(closing[bracket_type])
            else:  # Second half: matching closing brackets
                brackets.append(stack.pop())
                
        return "".join(brackets), "1"
        
    elif case_type == "always_unbalanced":
        # Generate clearly unbalanced brackets
        n = random.randint(3, 10)
        brackets = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        
        # Add n opening brackets
        for _ in range(n):
            brackets.append(random.choice(opening))
        # Add n-1 closing brackets
        for _ in range(n-1):
            brackets.append(random.choice(closing))
            
        return "".join(brackets), "0"
        
    elif case_type == "empty":
        # Empty string is considered balanced
        return "", "1"
        
    else:  # random
        n = random.randint(4, 20)
        brackets = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        stack = []
        
        for _ in range(n):
            if not stack or random.random() < 0.6:  # 60% chance of opening bracket
                bracket_type = random.randint(0, 2)
                brackets.append(opening[bracket_type])
                stack.append(closing[bracket_type])
            else:  # Close a bracket
                brackets.append(stack.pop())
                
        # Randomly decide whether to make it unbalanced
        make_unbalanced = random.random() < 0.4  # 40% chance
        if make_unbalanced:
            if random.random() < 0.5:  # Add extra closing bracket
                brackets.append(random.choice(closing))
            else:  # Leave some brackets unclosed
                stack_size = len(stack)
                if stack_size > 0:
                    stack = stack[:-random.randint(1, stack_size)]
                    
        # Add remaining closing brackets if we want it balanced
        if not make_unbalanced:
            brackets.extend(reversed(stack))
            
        return "".join(brackets), "1" if is_balanced("".join(brackets)) else "0"

def generate_test_cases() -> List[Dict]:
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example case
    test_cases.append({
        "input": "1\n{[()]}",
        "output": "1"
    })
    
    # Test case 2: Multiple test cases with different types
    cases = [
        generate_test_case("always_balanced"),
        generate_test_case("always_unbalanced"),
        generate_test_case("empty"),
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