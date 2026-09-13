class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        parens = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:
            if char in parens:
                if stack and stack[-1] == parens[char]:
                    stack.pop()
                    continue
                else:
                    return False
            
            stack.append(char)

        return not stack