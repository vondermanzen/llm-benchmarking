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
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Set of opening brackets for quick lookup
    opening_brackets = {'(', '[', '{'}
    
    for bracket in brackets:
        if bracket in opening_brackets:
            # If it's an opening bracket, push to stack
            stack.append(bracket)
        elif bracket in bracket_pairs:
            # If it's a closing bracket
            if not stack:
                # No matching opening bracket
                return False
            
            # Check if the most recent opening bracket matches
            if stack[-1] != bracket_pairs[bracket]:
                # Mismatched bracket types
                return False
            
            # Remove the matched opening bracket from stack
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