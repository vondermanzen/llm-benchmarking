#!/usr/bin/env python3
import os
import sys
import subprocess
from datetime import datetime
import re
from collections import defaultdict

def find_benchmark_dirs():
    """Find all directories containing benchmarking.py files."""
    return [d for d in os.listdir('.')
            if os.path.isdir(d) and os.path.exists(os.path.join(d, 'benchmarking.py'))]

def parse_benchmark_output(output):
    """Parse the benchmark output to extract scores and times for each solution."""
    results = {}
    
    # Split output into lines
    lines = output.split('\n')
    
    # Look for lines with score and time patterns
    for line in lines:
        # Match pattern like "script.py    5/7     123.45"
        match = re.match(r'(\w+\.py)\s+(\d+)/(\d+)\s+(\d+\.?\d*)', line)
        if match:
            script_name = match.group(1)
            correct = int(match.group(2))
            total = int(match.group(3))
            avg_time = float(match.group(4))
            
            results[script_name] = {
                'correct': correct,
                'total': total,
                'avg_time': avg_time
            }
    
    return results

def calculate_adjusted_score(results):
    """Calculate adjusted scores based on correctness and speed."""
    adjusted_scores = {}
    
    # Find the fastest time to use as baseline
    fastest_time = float('inf')
    for result in results.values():
        if result['avg_time'] < fastest_time:
            fastest_time = result['avg_time']
    
    # If no valid times found, use a default baseline
    if fastest_time == float('inf'):
        fastest_time = 10  # 10ms baseline
    
    for script, result in results.items():
        # Base score is the number of correct answers
        base_score = result['correct']
        
        # Linear time penalty: score is inversely proportional to execution time
        # Fastest solution gets full points, others get proportionally less
        if result['avg_time'] < float('inf'):
            time_penalty = fastest_time / result['avg_time']
        else:
            time_penalty = 0.5  # Maximum penalty for failed solutions
        
        # Calculate final adjusted score
        adjusted_score = base_score * time_penalty
        
        # Divide Grok's score by 2
        if script == 'grok.py':
            adjusted_score /= 2
        
        adjusted_scores[script] = round(adjusted_score, 2)
    
    return adjusted_scores

def run_benchmarks():
    # Get the script's directory
    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)
    
    print(f"\nRunning benchmarks from: {root_dir}")
    print("=" * 60)
    
    # Find all benchmark directories
    benchmark_dirs = find_benchmark_dirs()
    if not benchmark_dirs:
        print("No benchmarks found!")
        return
    
    print(f"Found {len(benchmark_dirs)} benchmarks to run\n")
    
    # Store results for each problem
    all_results = {}
    
    # Run each benchmark
    for directory in benchmark_dirs:
        print(f"\nRunning benchmark in {directory}:")
        print("-" * 40)
        
        # Store current directory
        original_dir = os.getcwd()
        try:
            # Change to benchmark directory and run
            os.chdir(os.path.join(root_dir, directory))
            result = subprocess.run(
                [sys.executable, 'benchmarking.py', '--no-details'],
                capture_output=True,
                text=True,
                check=True
            )
            
            # Print the benchmark output
            print(result.stdout)
            
            # Parse results for this problem
            problem_results = parse_benchmark_output(result.stdout)
            if problem_results:
                all_results[directory] = problem_results
            else:
                print(f"Warning: No results parsed from {directory}")
                
        except subprocess.CalledProcessError as e:
            print(f"Error running benchmark in {directory}: {e}")
            if e.stdout:
                print("Output:", e.stdout)
            if e.stderr:
                print("Error:", e.stderr)
        except Exception as e:
            print(f"Unexpected error in {directory}: {e}")
        finally:
            # Always return to original directory
            os.chdir(original_dir)
    
    # Calculate and display final scores
    print("\n" + "=" * 60)
    print("FINAL SCORES (Adjusted for Speed)")
    print("=" * 60)
    
    # Aggregate scores across all problems
    total_scores = defaultdict(float)
    for problem, results in all_results.items():
        adjusted_scores = calculate_adjusted_score(results)
        for script, score in adjusted_scores.items():
            total_scores[script] += score
    
    # Display final scores
    if total_scores:
        print(f"\n{'Script':<20} {'Total Score':<15}")
        print("-" * 35)
        for script, score in sorted(total_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{script:<20} {score:<15.2f}")
    else:
        print("\nNo scores were calculated. Check if any benchmarks produced valid results.")
    
    print("\n" + "=" * 60)
    print("Completed all benchmarks")
    print("=" * 60)

if __name__ == "__main__":
    run_benchmarks()
    # Keep console window open on Windows
    if sys.platform == 'win32':
        input("\nPress Enter to close this window...") 