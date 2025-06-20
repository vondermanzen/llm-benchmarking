#!/usr/bin/env python3
"""
Bracket Sequence Validator

A Python command-line program that validates whether bracket sequences 
are properly balanced using a stack-based algorithm.

Author: Generated Code
Date: June 20, 2025
"""


def is_balanced_brackets(sequence):
    """
    Check if a bracket sequence is properly balanced using stack algorithm.
    
    Args:
        sequence (str): String containing only brackets: '(', ')', '[', ']', '{', '}'
    
    Returns:
        bool: True if sequence is balanced, False otherwise
    """
    # Stack to keep track of opening brackets
    stack = []

    # Mapping of closing brackets to their corresponding opening brackets
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    # Set of opening brackets for quick lookup
    opening_brackets = {'(', '[', '{'}

    # Process each character in the sequence
    for char in sequence:
        if char in opening_brackets:
            # Push opening bracket onto stack
            stack.append(char)
        elif char in bracket_pairs:
            # Check if we have a matching opening bracket
            if not stack:
                # No opening bracket to match with this closing bracket
                return False

            # Pop the most recent opening bracket
            last_opening = stack.pop()

            # Check if the brackets match
            if last_opening != bracket_pairs[char]:
                # Mismatched bracket types (e.g., '[}')
                return False
        else:
            # Invalid character (shouldn't happen based on problem constraints)
            return False

    # Sequence is balanced if stack is empty (all brackets matched)
    return len(stack) == 0


def main():
    """
    Main function to handle input/output and run the bracket validation.
    """
    try:
        # Read the length of the bracket sequence
        n = int(input().strip())

        # Handle edge case: empty sequence
        if n == 0:
            print("YES")  # Empty sequence is considered balanced
            return

        # Read the bracket sequence
        sequence = input().strip()

        # Validate input length matches expected length
        if len(sequence) != n:
            print("NO")  # Input doesn't match expected length
            return

        # Validate that sequence contains only valid bracket characters
        valid_chars = {'(', ')', '[', ']', '{', '}'}
        if not all(char in valid_chars for char in sequence):
            print("NO")  # Invalid characters in sequence
            return

        # Check if the bracket sequence is balanced
        if is_balanced_brackets(sequence):
            print("YES")
        else:
            print("NO")

    except ValueError:
        # Handle case where N is not a valid integer
        print("NO")
    except EOFError:
        # Handle case where input is incomplete
        print("NO")
    except Exception:
        # Handle any other unexpected errors
        print("NO")


if __name__ == "__main__":
    main()