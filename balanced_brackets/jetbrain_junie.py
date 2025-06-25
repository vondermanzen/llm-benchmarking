def is_balanced(brackets):
    """
    Check if a sequence of brackets is properly balanced.

    Args:
        brackets (str): A string containing only bracket characters: '(', ')', '[', ']', '{', '}'

    Returns:
        bool: True if the brackets are balanced, False otherwise
    """
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for bracket in brackets:
        # If it's an opening bracket, push to stack
        if bracket in '([{':
            stack.append(bracket)
        # If it's a closing bracket
        elif bracket in ')]}':
            # If stack is empty or the top doesn't match, it's not balanced
            if not stack or stack.pop() != bracket_pairs[bracket]:
                return False

    # If stack is empty, all brackets were matched
    return len(stack) == 0

if __name__ == '__main__':
    # Read input
    n = int(input().strip())
    brackets = input().strip()

    # Check if brackets are balanced
    if is_balanced(brackets):
        print("YES")
    else:
        print("NO")

