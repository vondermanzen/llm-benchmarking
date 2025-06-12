def is_balanced(brackets):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for bracket in brackets:
        if bracket in '([{':
            stack.append(bracket)
        elif bracket in ')]}':
            if not stack or stack[-1] != bracket_pairs[bracket]:
                return False
            stack.pop()

    return len(stack) == 0

n = int(input().strip())
brackets = input().strip()

if is_balanced(brackets):
    print("YES")
else:
    print("NO")