def is_balanced(brackets):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or stack[-1] != pairs[bracket]:
                return "NO"
            stack.pop()
    
    return "YES" if not stack else "NO"

n = int(input())
brackets = input()
print(is_balanced(brackets))