def is_balanced(brackets):
    """
    Check if a sequence of brackets is properly balanced.

    Args:
        brackets (str): String containing only bracket characters

    Returns:
        bool: True if balanced, False otherwise
    """
    # Stack to keep track of opening brackets
    stack = []

    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    # Set of opening brackets for quick lookup
    opening_brackets = {'(', '[', '{'}

    for char in brackets:
        if char in opening_brackets:
            # Push opening bracket onto stack
            stack.append(char)
        elif char in bracket_pairs:
            # Check if we have a matching opening bracket
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            # Pop the matching opening bracket
            stack.pop()

    # If stack is empty, all brackets were properly matched
    return len(stack) == 0


def main():
    # Read input
    n = int(input().strip())
    brackets = input().strip()

    # Check if brackets are balanced and output result
    if is_balanced(brackets):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

