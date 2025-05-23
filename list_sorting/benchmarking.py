import subprocess
import os

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

results = {}

for file in py_files:
    correct = 0
    total = len(test_cases)
    for input_str, expected_output in test_cases:
        try:
            # Run the script with input and capture output
            result = subprocess.run(
                ['python', file],
                input=input_str.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5
            )
            output = result.stdout.decode().strip()
            if output == expected_output:
                correct += 1
        except Exception:
            pass  # Optionally log errors here

    results[file] = f"{correct}/{total}"

# Print summary of results
print("Script Evaluation Results:")
for script, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"{script}: {score}")
