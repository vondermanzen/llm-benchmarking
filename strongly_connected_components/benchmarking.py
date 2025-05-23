import sys
import random
from collections import defaultdict
from typing import List, Set, Dict, Tuple
import subprocess
import os

def generate_test_case(case_type: str = "random") -> Tuple[str, str]:
    """Generate a test case based on the type."""
    if case_type == "single_scc":
        # Generate a cycle
        n = random.randint(3, 10)
        edges = [(i, (i + 1) % n) for i in range(n)]
        return f"{n} {len(edges)}\n" + "\n".join(f"{u} {v}" for u, v in edges), "1"
        
    elif case_type == "no_edges":
        # Each node is its own SCC
        n = random.randint(5, 10)
        return f"{n} 0\n", str(n)
        
    elif case_type == "chain":
        # Chain of nodes, each node is its own SCC
        n = random.randint(5, 10)
        edges = [(i, i + 1) for i in range(n - 1)]
        return f"{n} {len(edges)}\n" + "\n".join(f"{u} {v}" for u, v in edges), str(n)
        
    elif case_type == "two_scc":
        # Two strongly connected components
        n = random.randint(6, 10)
        half = n // 2
        edges = [(i, (i + 1) % half) for i in range(half)]  # First SCC
        edges += [(i + half, ((i + 1) % half) + half) for i in range(half)]  # Second SCC
        edges.append((0, half))  # Connect them
        return f"{n} {len(edges)}\n" + "\n".join(f"{u} {v}" for u, v in edges), "2"
        
    else:  # random
        n = random.randint(5, 15)
        edge_count = random.randint(n, n * 2)
        edges = []
        for _ in range(edge_count):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            edges.append((u, v))
        return (
            f"{n} {len(edges)}\n" + "\n".join(f"{u} {v}" for u, v in edges),
            str(kosaraju_scc(n, edges))
        )

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
    
    # Run first DFS on all nodes
    for node in range(n):
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
    """Generate various test cases with their expected outputs."""
    test_cases = []
    
    # Test case 1: Example case
    test_cases.append({
        "input": "1\n4 4\n0 1\n1 2\n2 3\n3 1",
        "output": "2"
    })
    
    # Test case 2: Multiple test cases with different types
    cases = [
        generate_test_case("single_scc"),
        generate_test_case("no_edges"),
        generate_test_case("chain"),
        generate_test_case("two_scc"),
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