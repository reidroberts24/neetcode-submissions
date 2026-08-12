class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        while numset:
            cur = min(numset)
            seq_length = 1
            while cur + 1 in numset:
                numset.remove(cur)
                seq_length += 1
                cur += 1
            numset.remove(cur)
            longest = max(longest, seq_length)
        return longest
