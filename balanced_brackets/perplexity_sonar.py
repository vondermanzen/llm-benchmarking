for char in s:
    if char in pairs:
        stack.append(char)
    else:
        if not stack:
            print("NO")
            break
        top = stack.pop()
        if pairs[top] != char:
            print("NO")
            break
else:
    if not stack:
        print("YES")
    else:
        print("NO")