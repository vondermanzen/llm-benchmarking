def is_balanced(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            top_element = stack.pop()
            if mapping[char] != top_element:
                return False
    return not stack

n = int(input())
s = input()

if is_balanced(s):
    print("YES")
else:
    print("NO")