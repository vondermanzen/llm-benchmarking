def is_balanced(sequence):
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Stack to keep track of opening brackets
    stack = []
    
    for char in sequence:
        # If it's an opening bracket, push to stack
        if char in bracket_map.values():
            stack.append(char)
        # If it's a closing bracket
        elif char in bracket_map.keys():
            # If stack is empty or top of stack doesn't match, return False
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # If stack is empty, all brackets are balanced
    return len(stack) == 0

# Read input
N = int(input())
sequence = input().strip()

# Check if sequence is balanced
result = "YES" if is_balanced(sequence) else "NO"
print(result)
