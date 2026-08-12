class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []
        backward = []

        for c in s:
            if not c.isalnum():
                continue
            forward.append(c.lower())
        
        for c in s[-1::-1]:
            if not c.isalnum():
                continue
            backward.append(c.lower())

        return backward == forward
