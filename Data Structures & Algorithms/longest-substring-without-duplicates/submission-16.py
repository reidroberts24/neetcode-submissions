class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # for loop for right pointer, while loop to shift left pointer whenever a duplicate is found
        cur_chars = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in cur_chars:
                cur_chars.remove(s[l])
                l += 1
            cur_chars.add(s[r])
            longest = max(longest, r - l + 1)
        return longest