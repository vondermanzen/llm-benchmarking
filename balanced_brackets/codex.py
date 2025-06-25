def is_balanced_brackets(n, sequence):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_map[char]:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

# Input reading
n = int(input())
sequence = input().strip()

# Output result
print(is_balanced_brackets(n, sequence))