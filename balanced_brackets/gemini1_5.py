def is_balanced(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return "NO"
        else:
            return "NO"  # Handle invalid characters if needed
    return "YES" if not stack else "NO"

n = int(input())
s = input()
print(is_balanced(s))