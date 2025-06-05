n = int(input().strip())
s = input().strip()

mapping = {')': '(', ']': '[', '}': '{'}
stack = []

for c in s:
    if c in '([{':
        stack.append(c)
    else:
        if not stack:
            print("NO")
            break
        if stack.pop() != mapping[c]:
            print("NO")
            break
else:
    if not stack:
        print("YES")
    else:
        print("NO")