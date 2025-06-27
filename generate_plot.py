#!/usr/bin/env python3
import subprocess
import sys
import re
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd
from assistant_mapping import TECHNICAL_TO_DISPLAY, DISPLAY_TO_COLOR, GENERAL_LLM_TECHNICAL_TO_DISPLAY

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
    """Create a bar chart for coding assistants using shared mapping and color legend. Also plot general LLMs in black and white with patterns."""
    if not scores:
        print("No scores found to plot!")
        return
    
    # Coding assistants (in mapping)
    filtered_scores = {k: v for k, v in scores.items() if k in TECHNICAL_TO_DISPLAY}
    display_scores = {TECHNICAL_TO_DISPLAY[k]: v for k, v in filtered_scores.items()}
    sorted_scores = dict(sorted(display_scores.items(), key=lambda x: x[1], reverse=True))
    colors = [DISPLAY_TO_COLOR[name] for name in sorted_scores.keys()]
    
    # Plot coding assistants
    plt.figure(figsize=(14, 8))
    names = list(sorted_scores.keys())
    values = list(sorted_scores.values())
    bars = plt.bar(names, values, color=colors)
    plt.title('Code Evaluation', fontsize=16, fontweight='bold')
    plt.xlabel('')
    plt.ylabel('Score (0-100)', fontsize=12, fontweight='bold')
    plt.xticks([])
    plt.ylim(0, 100)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                 f"{value:.1f}", ha='center', va='bottom', fontweight='bold')
    legend_handles = [plt.Rectangle((0,0),1,1, color=DISPLAY_TO_COLOR[name]) for name in names]
    plt.legend(legend_handles, names, title="Assistant", bbox_to_anchor=(1.05, 1), loc='upper left',
              handleheight=2.5, handlelength=3, borderaxespad=0.)
    plt.tight_layout()
    plt.savefig('coding_assistants.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\nPlot saved as 'coding_assistants.png'")

    # General LLMs (not in mapping)
    general_llms = {k: v for k, v in scores.items() if k not in TECHNICAL_TO_DISPLAY}
    if general_llms:
        # Use pretty names
        display_general = {GENERAL_LLM_TECHNICAL_TO_DISPLAY.get(k, k): v for k, v in general_llms.items()}
        sorted_general = dict(sorted(display_general.items(), key=lambda x: x[1], reverse=True))
        plt.figure(figsize=(14, 8))
        names = list(sorted_general.keys())
        values = list(sorted_general.values())
        patterns = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
        bars = []
        legend_handles = []
        for i, (name, value) in enumerate(zip(names, values)):
            bar = plt.bar(name, value, color='white', edgecolor='black',
                          hatch=patterns[i % len(patterns)])
            bars.append(bar)
            # Larger legend handle for better pattern visibility
            legend_handles.append(
                plt.Rectangle((0,0), 2, 1.2, facecolor='white', edgecolor='black', hatch=patterns[i % len(patterns)])
            )
        plt.title('Code Evaluation Reference (OpenRouter)', fontsize=16, fontweight='bold')
        plt.xlabel('')
        plt.ylabel('Score (0-100)', fontsize=12, fontweight='bold')
        plt.xticks([])
        plt.ylim(0, 100)
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        for bar, value in zip(bars, values):
            rect = bar[0]
            plt.text(rect.get_x() + rect.get_width()/2, rect.get_height() + 0.5, 
                     f"{value:.1f}", ha='center', va='bottom', fontweight='bold')
        plt.legend(
            legend_handles, names, title="Model",
            bbox_to_anchor=(1.05, 1), loc='upper left',
            handleheight=2.5, handlelength=3, borderaxespad=0.
        )
        plt.tight_layout()
        plt.savefig('general_llms.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Plot saved as 'general_llms.png'")

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
