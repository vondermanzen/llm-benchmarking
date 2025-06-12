def is_balanced(brackets):
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = {")": "(", "}": "{", "]": "["}
    
    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        elif bracket in closing:
            if not stack or stack.pop() != pairs[bracket]:
                return False
    
    return len(stack) == 0

N = int(input())
brackets = input().strip()

if is_balanced(brackets):
    print("YES")
else:
    print("NO")