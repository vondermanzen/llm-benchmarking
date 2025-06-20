def is_balanced(brackets):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or stack[-1] != matching_brackets[bracket]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"

# Read input
n = int(input())
brackets = input()

# Check if brackets are balanced
print(is_balanced(brackets))