class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []
        backward = []

        for c in s:
            if not c.isalnum():
                continue
            forward.append(c.lower())
        
        j = 0
        for c in s[-1::-1]:
            if not c.isalnum():
                continue
            if c.lower() != forward[j]:
                return False
            j += 1

        return True
