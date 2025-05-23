import sys
import random
from collections import defaultdict
from typing import List, Set, Dict

def generate_test_case(n: int, m: int, case_type: str = "random") -> str:
    """Generate a test case with n vertices and m edges."""
    edges = set()
    test_input = f"{n} {m}\n"
    
    if case_type == "single_scc":
        # Generate a single strongly connected component
        vertices = list(range(1, n + 1))
        random.shuffle(vertices)
        for i in range(n):
            edges.add((vertices[i], vertices[(i + 1) % n]))
        
        # Add remaining random edges if needed
        while len(edges) < m:
            u = random.randint(1, n)
            v = random.randint(1, n)
            edges.add((u, v))
            
    elif case_type == "chain":
        # Generate a chain of SCCs
        for i in range(1, n):
            edges.add((i, i + 1))
            
    else:  # random
        while len(edges) < m:
            u = random.randint(1, n)
            v = random.randint(1, n)
            edges.add((u, v))
    
    for u, v in edges:
        test_input += f"{u} {v}\n"
    return test_input.strip()

def kosaraju_scc(n: int, edges: List[tuple]) -> int:
    """
    Implementation of Kosaraju's algorithm to find the number of SCCs.
    This serves as the reference solution.
    """
    def dfs_forward(node: int, visited: Set[int], order: List[int]):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_forward(neighbor, visited, order)
        order.append(node)
    
    def dfs_reverse(node: int, visited: Set[int]):
        visited.add(node)
        for neighbor in reverse_graph[node]:
            if neighbor not in visited:
                dfs_reverse(neighbor, visited)
    
    # Build adjacency lists for original and reversed graphs
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)
    
    # First DFS to get finishing order
    visited = set()
    order = []
    for node in range(1, n + 1):
        if node not in visited:
            dfs_forward(node, visited, order)
    
    # Second DFS on reversed graph
    visited = set()
    scc_count = 0
    for node in reversed(order):
        if node not in visited:
            dfs_reverse(node, visited)
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
    
    # Test case 1: Example from prompt
    test_cases.append({
        "input": "4 4\n1 2\n2 3\n3 1\n4 1",
        "output": "2"
    })
    
    # Test case 2: Empty graph
    test_cases.append({
        "input": "5 0",
        "output": "5"
    })
    
    # Test case 3: Single SCC
    test_cases.append({
        "input": generate_test_case(5, 10, "single_scc"),
        "output": "1"
    })
    
    # Test case 4: Chain of SCCs
    test_cases.append({
        "input": generate_test_case(6, 5, "chain"),
        "output": "6"
    })
    
    # Test case 5: Large random graph
    test_cases.append({
        "input": generate_test_case(100, 300),
        "output": None  # Will be computed
    })
    
    # Compute expected outputs for generated test cases
    for case in test_cases:
        if case["output"] is None:
            lines = case["input"].strip().split("\n")
            n, m = map(int, lines[0].split())
            edges = []
            for i in range(m):
                u, v = map(int, lines[i + 1].split())
                edges.append((u, v))
            case["output"] = str(kosaraju_scc(n, edges))
    
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
                thread.join(timeout=2)  # 2 second timeout
                
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