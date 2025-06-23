def is_balanced(brackets):
    stack = []
    opening = set('([{')
    matching = {'}': '{', ']': '[', ')': '('}

    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        else:
            if not stack or matching[bracket] != stack.pop():
                return "NO"

    return "YES" if not stack else "NO"


N = int(input())
brackets_sequence = input()

assert 1 <= N <= 10000, "Input length must be between 1 and 10,000"
assert len(brackets_sequence) == N, "Input length does not match declared length"

print(is_balanced(brackets_sequence))