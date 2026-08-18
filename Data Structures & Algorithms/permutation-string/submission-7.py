class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_counts = {}
        s2_substr_counts = {}
        for r in range(len(s1)):
            s1_counts[s1[r]] = s1_counts.get(s1[r], 0) + 1
            s2_substr_counts[s2[r]] = s2_substr_counts.get(s2[r], 0) + 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if s2_substr_counts == s1_counts:
                break
            s2_substr_counts[s2[r]] = s2_substr_counts.get(s2[r], 0) + 1
            s2_substr_counts[s2[l]] -= 1
            if s2_substr_counts[s2[l]] == 0:
                del s2_substr_counts[s2[l]]
            l += 1
        return s1_counts == s2_substr_counts