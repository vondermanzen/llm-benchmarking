def is_balanced(brackets):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in brackets:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return "NO"
        else:
            return "NO"
    
    return "YES" if not stack else "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    brackets = data[1]
    
    if n != len(brackets):
        print("NO")
    else:
        print(is_balanced(brackets))

if __name__ == "__main__":
    main()
