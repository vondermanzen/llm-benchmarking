N = int(input().strip())
seq = input().strip()

pairs = {')': '(', ']': '[', '}': '{'}
openers = set(pairs.values())
stack = []

balanced = True
for ch in seq:
    if ch in openers:
        stack.append(ch)
    elif ch in pairs:
        if not stack or stack[-1] != pairs[ch]:
            balanced = False
            break
        stack.pop()
    else:
        # Invalid character not bracket, but problem states only brackets so treat as imbalance
        balanced = False
        break

if balanced and not stack:
    print("YES")
else:
    print("NO")
