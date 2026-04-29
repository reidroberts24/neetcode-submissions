class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) #const
        for s in strs: #n strings
            freq = [0] * 26 #const
            for c in s: # m 
                freq[ord(c) - ord("a")] += 1 #const
            key = tuple(freq) #const
            res[key].append(s)
        return res.values()
        # Time: O(n * m)
        # Space: O(n * m)