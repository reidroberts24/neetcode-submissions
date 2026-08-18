class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        char_map = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for char in s:
            if char not in char_map:
                stack.append(char)
                continue
            if not stack:
                return False
            if char_map[char] != stack[-1]:
                return False
            stack.pop()
        return True if not stack else False
            