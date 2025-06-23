def balanced_brackets(brackets):
    stack = []
    for char in brackets:
        if char == '(':
            stack.append(char)
        elif char == '[':
            stack.append(char)
        elif char == '{':
            stack.append(char)
        elif char == ']':
            if stack[-1] != '[':
                return 'NO'
            stack.pop()
        elif char == '}':
            if stack[-1] != '{':
                return 'NO'
            stack.pop()
        elif char == ')':
            if stack[-1] != '(':
                return 'NO'
            stack.pop()
        else:
            continue
    if stack:
        return 'NO'
    return 'YES'

# Test cases
n = int(input())
brackets = input()
for _ in range(n):
    print(balanced_brackets(brackets))