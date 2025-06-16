class Solution:
    def checkBalancedBrackets(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            elif ch in ")}]":
                if not stack:
                    return False
                last = stack.pop()
                if (ch == "}" and last != "{") or (ch == "]" and last != "[") or (ch == "}" and last != "("):
                    return False
        return not stack