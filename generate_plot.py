#!/usr/bin/env python3
import subprocess
import sys
import re
import matplotlib.pyplot as plt
from collections import defaultdict

def run_benchmarks():
    """Run the benchmark script and capture output with real-time display."""
    try:
        print("Starting benchmark process...")
        
        # Run with real-time output
        process = subprocess.Popen([sys.executable, 'run_all_tests.py'], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.STDOUT,
                                 text=True, 
                                 bufsize=1, 
                                 universal_newlines=True)
        
        output_lines = []
        
        # Read output line by line and display it
        for line in process.stdout:
            print(line.rstrip())  # Print to console in real-time
            output_lines.append(line)
        
        # Wait for process to complete
        process.wait()
        
        if process.returncode != 0:
            print(f"Benchmark process exited with code {process.returncode}")
            return None
            
        return ''.join(output_lines)
        
    except FileNotFoundError:
        print("Error: run_all_tests.py not found!")
        return None
    except Exception as e:
        print(f"Error running benchmarks: {e}")
        return None

def parse_scores(output):
    """Parse the benchmark output to extract scores for each LLM."""
    scores = defaultdict(int)
    
    # Split output into lines
    lines = output.split('\n')
    
    # Look for lines with score patterns like "chatgpt.py: 15/15"
    score_pattern = r'(\w+\.py):\s*(\d+)/(\d+)'
    
    for line in lines:
        match = re.search(score_pattern, line)
        if match:
            llm_name = match.group(1).replace('.py', '')  # Remove .py extension
            score = int(match.group(2))
            scores[llm_name] += score
    
    return dict(scores)

def create_plot(scores):
    """Create a bar chart of the scores, sorted by performance."""
    if not scores:
        print("No scores found to plot!")
        return
    
    # Sort by score (descending)
    sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    
    # Extract LLM names and scores
    llms = list(sorted_scores.keys())
    score_values = list(sorted_scores.values())
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    bars = plt.bar(llms, score_values, color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#593E2D', '#7209b7', '#16537e'])
    
    # Customize the plot
    plt.title('LLM Benchmark Results - Total Scores', fontsize=16, fontweight='bold')
    plt.xlabel('LLM', fontsize=12, fontweight='bold')
    plt.ylabel('Total Score', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on top of bars
    for bar, value in zip(bars, score_values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                str(value), ha='center', va='bottom', fontweight='bold')
    
    # Add grid for better readability
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('benchmark_results.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"\nPlot saved as 'benchmark_results.png'")

def main():
    print("Running benchmarks...")
    print("(This may take a while...)\n")
    
    output = run_benchmarks()
    
    if output is None:
        print("\nFailed to run benchmarks or get output.")
        return
    
    print("\n" + "="*60)
    print("ANALYZING RESULTS")
    print("="*60)
    
    scores = parse_scores(output)
    
    if scores:
        print("\nExtracted scores:")
        for llm, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{llm}: {score}")
        
        print("\nGenerating plot...")
        create_plot(scores)
    else:
        print("No scores could be extracted from the output!")
        print("Debug: Checking if output contains expected patterns...")
        if "Script Evaluation Results:" in output:
            print("Found 'Script Evaluation Results:' in output")
        else:
            print("Did not find 'Script Evaluation Results:' in output")

if __name__ == "__main__":
    main() 