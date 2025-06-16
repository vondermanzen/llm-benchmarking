def is_balanced(s):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for bracket in s:
        if bracket in brackets:
            stack.append(bracket)
        elif len(stack) == 0 or brackets[stack.pop()] != bracket:
            return "NO"
    return "YES" if len(stack) == 0 else "NO"

N = int(input().strip())
s = input().strip()
print(is_balanced(s))