def is_balanced(brackets):
    s = []
    mapping = {'}': '{', ']': '[', ')': '('}
    for bracket in brackets:
        if bracket in mapping.values():
            s.append(bracket)
        elif len(s) == 0 or s.pop() != mapping[bracket]:
            return False
    return len(s) == 0

n = int(input())
brackets = input()
if is_balanced(brackets):
    print('YES')
else:
    print('NO')