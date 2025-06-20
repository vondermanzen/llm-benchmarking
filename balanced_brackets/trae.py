def is_balanced(brackets):
    # Stack to keep track of opening brackets
    stack = []
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Iterate through each character in the input string
    for bracket in brackets:
        # If it's an opening bracket, push to stack
        if bracket in '({[':
            stack.append(bracket)
        # If it's a closing bracket
        elif bracket in ')}]':
            # Check if stack is empty or brackets don't match
            if not stack or stack.pop() != bracket_pairs[bracket]:
                return 'NO'
    
    # After processing all brackets, stack should be empty for a balanced string
    return 'YES' if not stack else 'NO'

def main():
    try:
        # Read the length of the bracket string
        n = int(input().strip())
        
        # Read the bracket string
        brackets = input().strip()
        
        # Validate input length
        if len(brackets) != n:
            print('NO')
            return
        
        # Check if input contains only valid brackets
        if not all(c in '(){}[]' for c in brackets):
            print('NO')
            return
        
        # Print the result
        print(is_balanced(brackets))
        
    except ValueError:
        print('NO')

if __name__ == '__main__':
    main()
