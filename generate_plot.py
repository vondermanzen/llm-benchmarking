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
    raw_scores = {}
    
    # Split output into lines
    lines = output.split('\n')
    
    # First, collect raw scores from individual benchmark outputs
    raw_score_data = {}
    current_script = None
    
    for line in lines:
        # Look for "Script Evaluation Results:" sections
        if "Script Evaluation Results:" in line:
            current_script = None
            continue
        
        # Match pattern like "script.py    5/7     123.45"
        match = re.match(r'(\w+\.py)\s+(\d+)/(\d+)\s+(\d+\.?\d*)', line)
        if match:
            script_name = match.group(1).replace('.py', '')
            correct = int(match.group(2))
            total = int(match.group(3))
            
            if script_name not in raw_score_data:
                raw_score_data[script_name] = {'correct': 0, 'total': 0}
            
            raw_score_data[script_name]['correct'] += correct
            raw_score_data[script_name]['total'] += total
    
    # Now parse the final adjusted scores
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
                adjusted_score = float(match.group(2))
                
                # Get raw score from collected data
                raw_correct = raw_score_data.get(llm_name, {}).get('correct', 0)
                raw_total = raw_score_data.get(llm_name, {}).get('total',68)  # Default to 70 if not found
                
                # Normalize adjusted score to 0-100 scale, but keep raw score as actual points
                normalized_adjusted = (adjusted_score / 68) * 100  # Maximum score is 70
                raw_score = (raw_correct / 68) * 100  # Raw score as percentage of total possible
                
                scores[llm_name] = normalized_adjusted
                raw_scores[llm_name] = raw_score
    
    return scores, raw_scores

def create_plot(scores, raw_scores):
    """Create a bar chart for coding assistants using shared mapping and color legend. Also plot general LLMs in black and white with patterns."""
    if not scores:
        print("No scores found to plot!")
        return
    
    # Coding assistants (in mapping)
    filtered_scores = {k: v for k, v in scores.items() if k in TECHNICAL_TO_DISPLAY}
    display_scores = {TECHNICAL_TO_DISPLAY[k]: v for k, v in filtered_scores.items()}
    sorted_scores = dict(sorted(display_scores.items(), key=lambda x: x[1], reverse=True))
    colors = [DISPLAY_TO_COLOR[name] for name in sorted_scores.keys()]
    
    # Get corresponding raw scores (ordered by adjusted scores)
    display_raw_scores = {TECHNICAL_TO_DISPLAY[k]: raw_scores[k] for k, v in filtered_scores.items()}
    raw_values = [display_raw_scores[name] for name in sorted_scores.keys()]
    
    # Plot coding assistants with stacked bars
    plt.figure(figsize=(14, 8))
    names = list(sorted_scores.keys())
    adjusted_values = list(sorted_scores.values())
    
    # Create stacked bars: adjusted score (bottom) + penalty component (top)
    penalty_values = [max(0, raw - adj) for raw, adj in zip(raw_values, adjusted_values)]
    
    # Plot adjusted score as the base (this is what we're ordering by)
    bars_adjusted = plt.bar(names, adjusted_values, color=colors, alpha=0.7, label='Final Score')
    
    # Plot penalty component on top (if any)
    if any(p > 0 for p in penalty_values):
        bars_penalty = plt.bar(names, penalty_values, bottom=adjusted_values, 
                              color='red', alpha=0.2, label='Raw Correctness Bonus')
    
    plt.title('Code Evaluation', fontsize=16, fontweight='bold')
    plt.xlabel('')
    plt.ylabel('Score (0-100)', fontsize=12, fontweight='bold')
    plt.xticks(range(len(names)), names, rotation=45, ha='right')
    plt.ylim(0, 100)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add value labels on top of bars
    for i, (name, adj_val, raw_val) in enumerate(zip(names, adjusted_values, raw_values)):
        plt.text(i, adj_val + 0.5, f"{adj_val:.1f}", ha='center', va='bottom', fontweight='bold')
    
    # Create legend for assistants
    legend_handles = [plt.Rectangle((0,0),1,1, color=DISPLAY_TO_COLOR[name]) for name in names]
    # Add legend entry for raw correctness bonus at the top
    legend_handles.insert(0, plt.Rectangle((0,0),1,1, color='red', alpha=0.2))
    legend_names = ['Code Correctness'] + names
    plt.legend(legend_handles, legend_names, bbox_to_anchor=(1.05, 1), loc='upper left',
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
        
        # Get corresponding raw scores for general LLMs (ordered by adjusted scores)
        display_general_raw = {GENERAL_LLM_TECHNICAL_TO_DISPLAY.get(k, k): raw_scores[k] for k, v in general_llms.items()}
        general_raw_values = [display_general_raw[name] for name in sorted_general.keys()]
        
        plt.figure(figsize=(14, 8))
        names = list(sorted_general.keys())
        adjusted_values = list(sorted_general.values())
        
        # Create stacked bars for general LLMs
        penalty_values = [max(0, raw - adj) for raw, adj in zip(general_raw_values, adjusted_values)]
        
        patterns = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*',
 '\\+x', '\\|*', '+o.', 'O.', '-.', '|.*', '|-o', '|-', '\\o*', 'oO',
 '/\\', '/xO', '\\o.', '/+O', '\\-.', '-xo', 'oO.', '/-+', '\\|.', '|o']
        bars_adjusted = []
        bars_penalty = []
        legend_handles = []
        
        for i, (name, adj_val, raw_val) in enumerate(zip(names, adjusted_values, general_raw_values)):
            # Plot adjusted score as the base
            bar_adjusted = plt.bar(name, adj_val, color='white', edgecolor='black',
                                  hatch=patterns[i % len(patterns)], alpha=0.7)
            bars_adjusted.append(bar_adjusted)
            
            # Plot penalty component if any
            penalty_val = max(0, raw_val - adj_val)
            if penalty_val > 0:
                bar_penalty = plt.bar(name, penalty_val, bottom=adj_val, color='red', alpha=0.2)
                bars_penalty.append(bar_penalty)
            
            # Create legend handle
            legend_handles.append(
                plt.Rectangle((0,0), 2, 1.2, facecolor='white', edgecolor='black', 
                            hatch=patterns[i % len(patterns)])
            )
        
        plt.title('Code Evaluation Reference (OpenRouter)', fontsize=16, fontweight='bold')
        plt.xlabel('')
        plt.ylabel('Score (0-100)', fontsize=12, fontweight='bold')
        plt.xticks(range(len(names)), names, rotation=45, ha='right')
        plt.ylim(0, 100)
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels
        for i, (name, adj_val, raw_val) in enumerate(zip(names, adjusted_values, general_raw_values)):
            plt.text(i, adj_val + 0.5, f"{adj_val:.1f}", ha='center', va='bottom', fontweight='bold')
        
        plt.legend(
            [plt.Rectangle((0,0),1,1, color='red', alpha=0.2)] + legend_handles, 
            ['Code Correctness'] + names,
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
    
    scores, raw_scores = parse_scores(output)
    
    if scores:
        print("\nExtracted scores:")
        for llm, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{llm}: {score:.2f}")
        
        print("\nGenerating plot...")
        create_plot(scores, raw_scores)
    else:
        print("No scores could be extracted from the output!")
        print("Debug: Checking if output contains expected patterns...")
        if "FINAL SCORES" in output:
            print("Found 'FINAL SCORES' in output")
        else:
            print("Did not find 'FINAL SCORES' in output")

if __name__ == "__main__":
    main() 
