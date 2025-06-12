n = int(input())
s = input().strip()

stack = []
balanced = True
mapping = {')': '(', ']': '[', '}': '{'}

for char in s:
    if char in ['(', '[', '{']:
        stack.append(char)
    else:
        if not stack or stack[-1] != mapping[char]:
            balanced = False
            break
        stack.pop()

if balanced and not stack:
    print("YES")
else:
    print("NO")