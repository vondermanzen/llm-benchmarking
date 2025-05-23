import sys
import random
from typing import List, Dict, Optional

def is_balanced(brackets: str) -> bool:
    """Reference solution to check if brackets are balanced."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for bracket in brackets:
        if bracket in '({[':
            stack.append(bracket)
        else:  # closing bracket
            if not stack:  # no matching opening bracket
                return False
            if stack[-1] != pairs[bracket]:  # mismatched brackets
                return False
            stack.pop()
    
    return len(stack) == 0  # check if all brackets were matched

def generate_test_case(n: int, case_type: str = "random") -> str:
    """Generate a test case of length n."""
    if case_type == "balanced":
        # Generate a balanced sequence
        stack = []
        brackets = []
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        pairs = dict(zip(opening, closing))
        
        # Ensure even length
        n = (n // 2) * 2
        
        for i in range(n):
            if len(stack) == 0 or (i < n - 1 and random.random() < 0.6):
                # Add opening bracket
                bracket = random.choice(opening)
                stack.append(bracket)
                brackets.append(bracket)
            else:
                # Add matching closing bracket
                bracket = pairs[stack.pop()]
                brackets.append(bracket)
                
        return f"{n}\n{''.join(brackets)}"
        
    elif case_type == "unbalanced":
        # Generate an unbalanced sequence
        brackets = []
        all_brackets = ['(', ')', '[', ']', '{', '}']
        
        # Choose type of unbalanced sequence
        error_type = random.choice([
            "mismatched",  # e.g., {[}]
            "unclosed",    # e.g., {[()
            "extra_closing"  # e.g., {[()]}]
        ])
        
        if error_type == "mismatched":
            # Generate a sequence with mismatched brackets
            brackets = list("{[()]}") # start with valid sequence
            # Swap two random positions
            i, j = random.sample(range(len(brackets)), 2)
            brackets[i], brackets[j] = brackets[j], brackets[i]
        elif error_type == "unclosed":
            # Generate sequence with unclosed brackets
            opening = ['(', '[', '{']
            for _ in range(n):
                brackets.append(random.choice(opening))
        else:  # extra_closing
            # Generate sequence with extra closing brackets
            closing = [')', ']', '}']
            for _ in range(n):
                brackets.append(random.choice(closing))
                
        return f"{len(brackets)}\n{''.join(brackets)}"
        
    else:  # random
        # Generate completely random sequence
        all_brackets = ['(', ')', '[', ']', '{', '}']
        brackets = [random.choice(all_brackets) for _ in range(n)]
        return f"{n}\n{''.join(brackets)}"

def verify_solution(test_input: str, expected_output: str, received_output: str) -> bool:
    """Verify if the received output matches the expected output."""
    try:
        # Parse input
        lines = test_input.strip().split("\n")
        n = int(lines[0])
        brackets = lines[1]
        
        # Check if brackets are actually balanced
        is_actually_balanced = is_balanced(brackets)
        
        # Parse and check output
        received = received_output.strip()
        return (received == "YES" and is_actually_balanced) or (received == "NO" and not is_actually_balanced)
        
    except:
        return False

def generate_test_cases() -> List[Dict]:
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example from prompt
    test_cases.append({
        "input": "6\n{[()]}",
        "output": "YES"
    })
    
    # Test case 2: Another example from prompt
    test_cases.append({
        "input": "4\n{[}]",
        "output": "NO"
    })
    
    # Test case 3: Third example from prompt
    test_cases.append({
        "input": "2\n)(", 
        "output": "NO"
    })
    
    # Test case 4: Empty sequence
    test_cases.append({
        "input": "0\n",
        "output": "YES"
    })
    
    # Test case 5: Single bracket
    test_cases.append({
        "input": "1\n(",
        "output": "NO"
    })
    
    # Test case 6: Large balanced sequence
    test_cases.append({
        "input": generate_test_case(100, "balanced"),
        "output": None
    })
    
    # Test case 7: Large unbalanced sequence
    test_cases.append({
        "input": generate_test_case(100, "unbalanced"),
        "output": None
    })
    
    # Test case 8: Random sequence
    test_cases.append({
        "input": generate_test_case(50, "random"),
        "output": None
    })
    
    # Compute expected outputs for generated test cases
    for case in test_cases:
        if case["output"] is None:
            lines = case["input"].strip().split("\n")
            brackets = lines[1] if len(lines) > 1 else ""
            case["output"] = "YES" if is_balanced(brackets) else "NO"
    
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
                    print(f"Input:")
                    print(case["input"])
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