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
    scores = {}
    
    # Split output into lines
    lines = output.split('\n')
    
    # Look for the final scores section
    in_final_scores = False
    for line in lines:
        if "FINAL SCORES (Adjusted for Speed)" in line:
            in_final_scores = True
            continue
        if in_final_scores and "Script" in line and "Total Score" in line:
            continue
        if in_final_scores and "-" * 35 in line:
            continue
        if in_final_scores and line.strip():
            # Match pattern like "script.py    58.00"
            match = re.match(r'(\w+\.py)\s+(\d+\.?\d*)', line)
            if match:
                llm_name = match.group(1).replace('.py', '')  # Remove .py extension
                score = float(match.group(2))
                # Normalize score to 0-100 scale
                normalized_score = (score / 70) * 100  # Assuming max score is around 70
                # Divide score by 2 if model name contains 'grok'
                if 'grok' in llm_name.lower():
                    normalized_score /= 2
                scores[llm_name] = normalized_score
    
    return scores

def create_plot(scores):
    """Create two separate bar charts - one for coding assistants and one for non-coding assistants."""
    if not scores:
        print("No scores found to plot!")
        return
    
    # Sort by score (descending)
    sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    
    # Define non-code assistants (all others are code assistants)
    non_code_assistants = {'deepseek_v3', 'gpt4', 'grok2', 'claude3_5sonnet', 'gemini2_0flash', 'meta_llama_3', 'qwen_vl_plus', 'phi4', 'nova_pro_v1'}
    
    # Split scores into two groups
    code_scores = {k: v for k, v in sorted_scores.items() if k not in non_code_assistants}
    non_code_scores = {k: v for k, v in sorted_scores.items() if k in non_code_assistants}
    
    # Add Cancre to both groups if it exists
    if 'cancre' in sorted_scores:
        code_scores['cancre'] = sorted_scores['cancre']
        non_code_scores['cancre'] = sorted_scores['cancre']
    
    # Plot coding assistants
    if code_scores:
        plt.figure(figsize=(12, 8))
        llms = list(code_scores.keys())
        score_values = list(code_scores.values())
        bars1 = plt.bar(llms, score_values, color='#ADD8E6')
        
        # Customize the plot
        plt.title('Coding Assistants Performance', fontsize=16, fontweight='bold')
        plt.xlabel('LLM', fontsize=12, fontweight='bold')
        plt.ylabel('Score (0-100)', fontsize=12, fontweight='bold')
        plt.xticks(rotation=45, ha='right')
        plt.ylim(0, 100)
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels on top of bars
        for bar, value in zip(bars1, score_values):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    f"{value:.1f}", ha='center', va='bottom', fontweight='bold')
        
        # Adjust layout and save
        plt.tight_layout()
        plt.savefig('coding_assistants.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    # Plot non-coding assistants
    if non_code_scores:
        plt.figure(figsize=(12, 8))
        llms = list(non_code_scores.keys())
        score_values = list(non_code_scores.values())
        bars2 = plt.bar(llms, score_values, color='#87CEEB')
        
        # Customize the plot
        plt.title('General LLMs Performance', fontsize=16, fontweight='bold')
        plt.xlabel('LLM', fontsize=12, fontweight='bold')
        plt.ylabel('Score (0-100)', fontsize=12, fontweight='bold')
        plt.xticks(rotation=45, ha='right')
        plt.ylim(0, 100)
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels on top of bars
        for bar, value in zip(bars2, score_values):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    f"{value:.1f}", ha='center', va='bottom', fontweight='bold')
        
        # Adjust layout and save
        plt.tight_layout()
        plt.savefig('general_llms.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    print(f"\nPlots saved as 'coding_assistants.png' and 'general_llms.png'")

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
            print(f"{llm}: {score:.2f}")
        
        print("\nGenerating plot...")
        create_plot(scores)
    else:
        print("No scores could be extracted from the output!")
        print("Debug: Checking if output contains expected patterns...")
        if "FINAL SCORES" in output:
            print("Found 'FINAL SCORES' in output")
        else:
            print("Did not find 'FINAL SCORES' in output")

if __name__ == "__main__":
    main() 