def solve_balanced_brackets():
    # First line: N (length of the bracket sequence)
    # This line is read, but N itself might not be strictly needed
    # if len(sequence) is used for checks.
    # For competitive programming, always read all specified inputs.
    try:
        _ = input() # Consume the line for N (length)
    except EOFError:
        # This typically won't happen with contest system's stdin
        print("NO") 
        return

    # Second line: the bracket sequence itself
    try:
        sequence = input()
    except EOFError:
        print("NO")
        return

    stack = []
    # Maps closing brackets to their corresponding opening brackets
    bracket_map = {")": "(", "]": "[", "}": "{"}
    
    # An empty sequence is explicitly stated as balanced.
    if not sequence:
        print("YES")
        return

    for char in sequence:
        if char in "([{":  # If char is an opening bracket
            stack.append(char)
        elif char in ")]}":  # If char is a closing bracket
            # If stack is empty (no matching opening bracket)
            # or if the top of stack is not the correct opening bracket
            if not stack or stack.pop() != bracket_map[char]:
                print("NO")
                return
        # According to the problem, the input consists ONLY of brackets.
        # No need for an 'else' case to handle invalid characters.

    # After iterating through the sequence:
    # If stack is empty, all brackets were matched and popped. -> Balanced
    # If stack is not empty, there are unclosed opening brackets. -> Not Balanced
    if not stack:
        print("YES")
    else:
        print("NO")

# Execute the solution function
solve_balanced_brackets()