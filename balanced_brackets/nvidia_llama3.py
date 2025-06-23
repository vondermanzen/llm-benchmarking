def is_balanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for bracket in s:
        if bracket in bracket_map.values():
            stack.append(bracket)
        elif bracket in bracket_map:
            if not stack or stack.pop() != bracket_map[bracket]:
                return "NO"
    return "YES" if not stack else "NO"

n = int(input())
s = input()
print(is_balanced(s))