def is_balanced(brackets):
    stack = []
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    
    for bracket in brackets:
        if bracket in bracket_map:
            stack.append(bracket)
        elif len(stack) == 0 or bracket_map[stack.pop()] != bracket:
            return "NO"
    
    return "YES" if len(stack) == 0 else "NO"

if __name__ == "__main__":
    n = int(input())
    brackets = input()
    result = is_balanced(brackets)
    print(result)