def is_balanced(brackets):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for bracket in brackets:
        if bracket in '([{':
            stack.append(bracket)
        elif bracket in ')]}':
            if not stack or stack.pop() != pairs[bracket]:
                return False
    
    return len(stack) == 0

def main():
    n = int(input())
    brackets = input()
    
    if is_balanced(brackets):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()