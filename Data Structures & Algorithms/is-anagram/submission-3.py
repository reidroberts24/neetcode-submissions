class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            hashmap = {}
            for i in range(len(s)):
                hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
            
            for i in range(len(t)):
                if t[i] not in hashmap:
                    return False
                hashmap[t[i]] -= 1
            
            for key, val in hashmap.items():
                if val != 0:
                    return False
            return True
        return False
        
