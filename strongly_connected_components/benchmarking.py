import sys
from collections import defaultdict
from typing import List, Set, Dict, Tuple
import subprocess
import os
import time

def kosaraju_scc(n: int, edges: List[Tuple[int, int]]) -> int:
    """Reference implementation of Kosaraju's algorithm."""
    
    # Build adjacency lists for graph and transpose
    graph = defaultdict(list)
    transpose = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        transpose[v].append(u)
    
    # First DFS to get finishing times
    visited = set()
    finish_order = []
    
    def dfs1(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs1(neighbor)
        finish_order.append(node)
    
    # Run first DFS on all nodes (1-based indexing)
    for node in range(1, n + 1):
        if node not in visited:
            dfs1(node)
    
    # Second DFS on transpose graph
    visited = set()
    scc_count = 0
    
    def dfs2(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in transpose[node]:
            dfs2(neighbor)
    
    # Process nodes in reverse finishing order
    for node in reversed(finish_order):
        if node not in visited:
            dfs2(node)
            scc_count += 1
    
    return scc_count

def verify_solution(test_input: str, expected_output: str, received_output: str) -> bool:
    """Verify if the received output matches the expected output."""
    try:
        received = int(received_output.strip())
        expected = int(expected_output.strip())
        return received == expected
    except:
        return False

def generate_test_cases() -> List[Dict]:
    """Generate hardcoded test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example from prompt
    test_cases.append({
        "input": "4 4\n1 2\n2 3\n3 1\n4 1",
        "output": "2",
        "description": "Example from prompt - 4 nodes with cycle 1→2→3→1 and isolated node 4"
    })
    
    # Test case 2: Single SCC (simple cycle)
    test_cases.append({
        "input": "3 3\n1 2\n2 3\n3 1",
        "output": "1",
        "description": "Single SCC - simple 3-node cycle"
    })
    
    # Test case 3: No edges (each node is its own SCC)
    test_cases.append({
        "input": "5 0\n",
        "output": "5",
        "description": "No edges - each of 5 nodes is its own SCC"
    })
    
    # Test case 4: Chain (linear graph)
    test_cases.append({
        "input": "4 3\n1 2\n2 3\n3 4",
        "output": "4",
        "description": "Linear chain - each node is its own SCC"
    })
    
    # Test case 5: Two SCCs
    test_cases.append({
        "input": "6 7\n1 2\n2 3\n3 1\n4 5\n5 6\n6 4\n1 4",
        "output": "2",
        "description": "Two SCCs - cycle {1,2,3} and cycle {4,5,6} connected by edge 1→4"
    })
    
    # Test case 6: Complex case with multiple SCCs
    test_cases.append({
        "input": "8 10\n1 2\n2 1\n3 4\n4 5\n5 3\n6 7\n7 8\n8 6\n2 3\n5 6",
        "output": "3",
        "description": "Three SCCs - {1,2}, {3,4,5}, {6,7,8} with connecting edges"
    })
    
    # Test case 7: Single node
    test_cases.append({
        "input": "1 0\n",
        "output": "1",
        "description": "Single node - trivial SCC"
    })
    
    # Test case 8: Self loops
    test_cases.append({
        "input": "3 3\n1 1\n2 2\n3 3",
        "output": "3",
        "description": "Self loops - each node with self-loop is its own SCC"
    })
    
    # Test case 9: Larger single SCC
    test_cases.append({
        "input": "5 5\n1 2\n2 3\n3 4\n4 5\n5 1",
        "output": "1",
        "description": "Large single SCC - 5-node cycle"
    })
    
    # Test case 10: Mixed case
    test_cases.append({
        "input": "7 8\n1 2\n2 1\n3 4\n4 3\n5 6\n6 7\n7 5\n2 3",
        "output": "3",
        "description": "Mixed case - three SCCs {1,2}, {3,4}, and {5,6,7} with one-way edge 2→3"
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