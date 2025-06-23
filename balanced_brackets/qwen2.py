def check_brackets(sequence):
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    open_brackets = set(['(', '[', '{'])
    stack = []
    for bracket in sequence:
        if bracket in open_brackets:
            stack.append(bracket)
        elif stack and bracket_map[stack[-1]] == bracket:
            stack.pop()
        else:
            return "NO"
    return "YES" if not stack else "NO"

# Reading input
N = int(input())
sequence = input()

# Checking and printing output
print(check_brackets(sequence))