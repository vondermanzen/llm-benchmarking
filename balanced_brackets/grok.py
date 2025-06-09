def is_balanced(n, sequence):
    # Stack to keep track of opening brackets
    stack = []
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    brackets = {')': '(', ']': '[', '}': '{'}
    
    # Iterate through each character in the sequence
    for char in sequence:
        # If it's an opening bracket, push to stack
        if char in '([{':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')]}':
            # If stack is empty or top of stack doesn't match
            if not stack or stack.pop() != brackets[char]:
                return "NO"
    
    # Sequence is balanced only if stack is empty
    return "YES" if not stack else "NO"

# Read input
n = int(input())
sequence = input().strip()

# Print result
print(is_balanced(n, sequence))