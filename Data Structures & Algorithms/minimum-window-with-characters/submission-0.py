class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        
        counts_t, counts_s = {}, {}

        for i in range(len(t)):
            counts_t[t[i]] = 1 + counts_t.get(t[i], 0)
        
        have, need = 0, len(counts_t)
        res, resLen = [-1, -1], float("-infinity")
        l = 0
        for r in range(len(s)):
            counts_s[s[r]] = 1 + counts_s.get(s[r], 0)
            if s[r] in counts_t and counts_t[s[r]] == counts_s[s[r]]:
                have += 1
            

            while have == need:
                resLen = max(resLen, r - l + 1)
                res = [l, r]
                counts_s[s[l]] -= 1
                if s[l] in counts_t and counts_s[s[l]] < counts_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l: r + 1] if resLen != float("-infinity") else ""