def is_balanced(brackets):
    # Dictionary to store matching bracket pairs
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Stack to keep track of opening brackets
    stack = []

    # Iterate through each bracket in the sequence
    for bracket in brackets:
        # If it's an opening bracket, push to stack
        if bracket in '([{':
            stack.append(bracket)
        # If it's a closing bracket
        elif bracket in ')]}':
            # If stack is empty or top of stack doesn't match
            if not stack or stack.pop() != bracket_pairs[bracket]:
                return False

    # Check if all brackets were matched (stack should be empty)
    return len(stack) == 0

def main():
    # Read input
    n = int(input())
    brackets = input().strip()

    # Validate input length
    if len(brackets) != n:
        print("NO")
        return

    # Check if brackets are balanced and print result
    result = "YES" if is_balanced(brackets) else "NO"
    print(result)

if __name__ == "__main__":
    main()
