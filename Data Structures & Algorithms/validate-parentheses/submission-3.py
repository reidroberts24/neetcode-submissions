class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map  = {')':'(', ']':'[','}':'{'}

        for c in s:
            if c not in char_map:
                stack.append(c)
                continue
            if not stack or stack[-1] != char_map[c]:
                return False
            stack.pop()
        return not stack
        