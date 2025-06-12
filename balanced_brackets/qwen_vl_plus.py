def check_bracket_balance(bracket_sequence):
    stack = []
    
    for char in bracket_sequence:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif len(stack) > 0:
            last_opened_char = stack.pop()
            match = {
                ')': '(',
                ']': '[',
                '}': '{'
            }
            
            if last_opened_char != match[char]:
                return False
    
    return True if len(stack) == 0 else False

N = int(input())
bracket_sequence = input().strip()

if check_bracket_balance(bracket_sequence):
    print("YES")
else:
    print("NO")