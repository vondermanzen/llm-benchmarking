def is_balanced(bracket_sequence):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for char in bracket_sequence:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    N = int(input())
    sequence = input().strip()
    print("YES" if is_balanced(sequence) else "NO")
