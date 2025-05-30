def is_balanced(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_map[char]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"

# Input reading
N = int(input())  # Length of bracket sequence
s = input().strip()
print(is_balanced(s))
