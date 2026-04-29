class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        if len(unique) < 2:
            return len(unique)
        longest = 0

        for i in unique:
            if i - 1 not in unique:
                seq = 1
                while i + 1 in unique:
                    seq += 1
                    longest = max(longest, seq)
                    i += 1
        return longest


