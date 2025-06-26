def is_balanced(brackets: str) -> str:
    stack = []
    # Mapping of closing to opening brackets
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in brackets:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return "NO"
            stack.pop()
        # If non-bracket character appears, according to problem this won't happen

    return "YES" if not stack else "NO"

def main():
    N = int(input())
    s = input().strip()
    print(is_balanced(s))

if __name__ == "__main__":
    main()