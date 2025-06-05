#!/usr/bin/env python3
import os
import sys
import subprocess
from datetime import datetime

def find_benchmark_dirs():
    """Find all directories containing benchmarking.py files."""
    return [d for d in os.listdir('.')
            if os.path.isdir(d) and os.path.exists(os.path.join(d, 'benchmarking.py'))]

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
    
    # Run each benchmark
    for directory in benchmark_dirs:
        print(f"\nRunning benchmark in {directory}:")
        print("-" * 40)
        
        # Store current directory
        original_dir = os.getcwd()
        try:
            # Change to benchmark directory and run
            os.chdir(os.path.join(root_dir, directory))
            subprocess.run([sys.executable, 'benchmarking.py'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running benchmark in {directory}: {e}")
        except Exception as e:
            print(f"Unexpected error in {directory}: {e}")
        finally:
            # Always return to original directory
            os.chdir(original_dir)
    
    print("\n" + "=" * 60)
    print("Completed all benchmarks")
    print("=" * 60)

if __name__ == "__main__":
    run_benchmarks()
    # Keep console window open on Windows
    if sys.platform == 'win32':
        input("\nPress Enter to close this window...") 