class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in brackets.values():
                stack.append(c)
            else:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0