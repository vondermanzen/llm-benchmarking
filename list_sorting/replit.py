#!/usr/bin/env python3
"""
Python script that sorts a list of integers in ascending order.

Usage:
    python sort_integers.py

Input Format:
    A single line containing space-separated integers.
    Example: 3 1 4 1 5 9

Output Format:
    A single line containing the sorted integers, space-separated.
    Example: 1 1 3 4 5 9

The script reads from standard input and writes to standard output.
"""

import sys


def main():
    """
    Main function that reads integers from stdin, sorts them, and outputs the result.
    """
    try:
        # Read input from standard input
        line = input().strip()
        
        # Handle empty input
        if not line:
            print("")
            return
        
        # Split the line into individual string tokens
        tokens = line.split()
        
        # Convert tokens to integers
        integers = []
        for token in tokens:
            try:
                integers.append(int(token))
            except ValueError:
                print(f"Error: '{token}' is not a valid integer", file=sys.stderr)
                sys.exit(1)
        
        # Sort the integers in ascending order
        sorted_integers = sorted(integers)
        
        # Convert back to strings and join with spaces
        result = ' '.join(map(str, sorted_integers))
        
        # Output the result
        print(result)
        
    except EOFError:
        # Handle case where no input is provided (Ctrl+D pressed)
        print("")
    except KeyboardInterrupt:
        # Handle case where user presses Ctrl+C
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()