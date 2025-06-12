def is_balanced(brackets):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {")": "(", "]": "[", "}": "{"}

    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or stack.pop() != bracket_pairs[bracket]:
                return "NO"

    return "YES" if not stack else "NO"


n = int(input())
brackets = input()

print(is_balanced(brackets))