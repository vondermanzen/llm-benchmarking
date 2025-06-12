def is_balanced(bracket_string):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for bracket in bracket_string:
        if bracket in matching_bracket.values():
            stack.append(bracket)
        elif bracket in matching_bracket.keys():
            if stack == [] or matching_bracket[bracket] != stack.pop():
                return "NO"
        else:
            return "NO"
    
    return "YES" if not stack else "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    bracket_string = data[1]
    
    result = is_balanced(bracket_string)
    print(result)

if __name__ == "__main__":
    main()