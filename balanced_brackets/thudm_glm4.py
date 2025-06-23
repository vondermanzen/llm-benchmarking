def is_balanced(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            if stack:
                top_element = stack.pop()
            else:
                top_element = '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

n = int(input())
s = input().strip()
if is_balanced(s):
    print("YES")
else:
    print("NO")