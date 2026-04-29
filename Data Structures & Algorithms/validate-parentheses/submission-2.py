class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_chars = set("([{")
        for char in s:
            if char in open_chars:
                stack.append(char)
            elif char == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False