def is_balanced(bracket_sequence: str) -> bool:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    opening = set(bracket_map.values())
    closing = set(bracket_map.keys())

    for char in bracket_sequence:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            # Ignore any non-bracket character (not expected per problem statement)
            continue
    return not stack

if __name__ == "__main__":
    N = int(input())
    sequence = input().strip()
    # Optional: check if input length matches N, but not required for problem
    print("YES" if is_balanced(sequence) else "NO")