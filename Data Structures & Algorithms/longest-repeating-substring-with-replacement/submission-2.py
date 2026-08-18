class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # determine the most freq character in window
        # move right pointer
        # check which char is still most freq
        # check if sum of all other chars <= k
        counts = {}
        longest = 0
        l = 0
        cur_most_frequent = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            cur_most_frequent = max(cur_most_frequent, counts[s[r]])
            while (r - l + 1) - cur_most_frequent > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
        