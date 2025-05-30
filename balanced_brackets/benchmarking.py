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
        
        # Generate nested structure
        def generate_nested(depth, max_depth):
            if depth >= max_depth or random.random() < 0.3:
                # Generate simple pair
                bracket_type = random.randint(0, 2)
                return opening[bracket_type] + closing[bracket_type]
            
            # Generate nested structure
            bracket_type = random.randint(0, 2)
            inner = generate_nested(depth + 1, max_depth)
            return opening[bracket_type] + inner + closing[bracket_type]
        
        result = generate_nested(0, 4)  # Up to 4 levels of nesting
        return result, "YES"
        
    elif case_type == "max_length":
        # Generate sequence close to max length (10,000)
        n = random.randint(9900, 10000)
        if n % 2 == 1:  # Ensure even length
            n -= 1
            
        brackets = []
        stack = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        
        # Fill first half with opening brackets
        for i in range(n // 2):
            bracket_type = random.randint(0, 2)
            brackets.append(opening[bracket_type])
            stack.append(closing[bracket_type])
            
        # Add matching closing brackets
        brackets.extend(reversed(stack))
        return "".join(brackets), "YES"
        
    elif case_type == "almost_balanced":
        # Generate almost balanced sequence with one error
        n = random.randint(10, 20)
        brackets = []
        stack = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        
        # Generate balanced sequence
        for i in range(n):
            if not stack or random.random() < 0.6:
                bracket_type = random.randint(0, 2)
                brackets.append(opening[bracket_type])
                stack.append(closing[bracket_type])
            else:
                brackets.append(stack.pop())
                
        # Add all remaining closing brackets
        brackets.extend(reversed(stack))
        
        # Introduce one error
        error_type = random.randint(0, 2)
        if error_type == 0:  # Wrong closing bracket
            pos = random.randint(0, len(brackets) - 1)
            while brackets[pos] not in closing:
                pos = random.randint(0, len(brackets) - 1)
            brackets[pos] = random.choice([c for c in closing if c != brackets[pos]])
        elif error_type == 1:  # Extra closing bracket
            pos = random.randint(0, len(brackets))
            brackets.insert(pos, random.choice(closing))
        else:  # Missing closing bracket
            pos = random.randint(0, len(brackets) - 1)
            while brackets[pos] not in closing:
                pos = random.randint(0, len(brackets) - 1)
            brackets.pop(pos)
            
        return "".join(brackets), "NO"
        
    elif case_type == "empty":
        # Empty string is considered balanced
        return "", "YES"
        
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
            
        return "".join(brackets), "YES" if is_balanced("".join(brackets)) else "NO"

def generate_test_cases() -> List[Dict]:
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Examples from prompt
    examples = [
        ("6\n{[()]}", "YES"),  # Example 1
        ("4\n{[}]", "NO"),     # Example 2
        ("2\n)(", "NO")        # Example 3
    ]
    for input_str, output in examples:
        test_cases.append({
            "input": input_str,
            "output": output
        })
    
    # Test case 2: Edge cases
    cases = [
        ("0\n", "YES"),  # Empty string
        ("1\n(", "NO"),  # Single opening bracket
        ("1\n)", "NO"),  # Single closing bracket
        ("2\n{}", "YES"),  # Simple pair
        ("6\n((()))", "YES")  # Multiple same type
    ]
    for input_str, output in cases:
        test_cases.append({
            "input": input_str,
            "output": output
        })
    
    # Test case 3: Special cases
    cases = [
        generate_test_case("always_balanced"),
        generate_test_case("almost_balanced"),
        generate_test_case("max_length")
    ]
    for input_str, output in cases:
        test_cases.append({
            "input": f"{len(input_str)}\n{input_str}",
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