def is_balanced(seq):
    stack = []
    for char in seq:
        if char in '({[':
            stack.append(char)
        elif not stack or stack.pop() != {')': '(', ']': '[', '}': '{'}(char):
            return False
    return not stack

n = int(input())
seq = input()
print('YES' if is_balanced(seq) else 'NO')