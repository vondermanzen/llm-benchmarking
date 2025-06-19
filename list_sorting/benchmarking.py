import subprocess
import os
import time
import sys

# Define test cases (input, expected output)
test_cases = [
    ("3 1 4 1 5 9", "1 1 3 4 5 9"),
    ("10 2 33 4 5", "2 4 5 10 33"),
    ("", ""),
    ("5 5 5 5", "5 5 5 5"),
    ("-3 -1 -2", "-3 -2 -1"),
    ("100 1", "1 100"),
    ("8 6 7 5 3 0 9", "0 3 5 6 7 8 9")
]

# Current benchmarking script's filename
benchmark_file = 'benchmarking.py'

# List all .py files in the current directory except this one
py_files = [f for f in os.listdir('.') if f.endswith('.py') and f != benchmark_file]

print(f"Found {len(py_files)} Python files to test: {', '.join(py_files)}")

results = {}

for file in py_files:
    print(f"\nTesting {file}...")
    correct = 0
    total = len(test_cases)
    total_time = 0
    any_failed = False
    
    for input_str, expected_output in test_cases:
        try:
            # Run the script with input and capture output
            start_time = time.time()
            result = subprocess.run(
                [sys.executable, file],  # Use sys.executable instead of 'python'
                input=input_str.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5
            )
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            output = result.stdout.decode().strip()
            if output == expected_output:
                correct += 1
            # Add time for all test cases, not just correct ones
            total_time += execution_time
        except Exception as e:
            any_failed = True
            print(f"  Error running {file}: {str(e)}")
            if hasattr(e, 'stderr') and e.stderr:
                print(f"    Error output: {e.stderr.decode().strip()}")

    # If any test case failed to execute, set total time to infinity
    if any_failed:
        total_time = float('inf')

    # Use total time for all test cases
    results[file] = {
        'score': f"{correct}/{total}",
        'total_time_ms': round(total_time, 2) if total_time != float('inf') else float('inf')
    }

# Print summary of results
print("\nScript Evaluation Results:")
print("-" * 50)
print(f"{'Script':<20} {'Score':<10} {'Total Time (ms)':<15}")
print("-" * 50)
for script, result in sorted(results.items(), key=lambda x: (x[1]['score'], -x[1]['total_time_ms']), reverse=True):
    print(f"{script:<20} {result['score']:<10} {result['total_time_ms']:<15.2f}")
