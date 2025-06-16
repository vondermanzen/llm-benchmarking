def is_balanced(s):
    stack = []
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_brackets = set(["(", "[", "{"])
    
    for i in s:
        if i in open_brackets:
            stack.append(i)
        elif len(stack) == 0 or bracket_map[stack.pop()] != i:
            return False
    return len(stack) == 0

n = int(input())
s = input()

if is_balanced(s):
    print("YES")
else:
    print("NO")