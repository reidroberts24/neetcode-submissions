class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        # insure starting from the smalles num by skipping the cur num if num - 1 in the set
        for n in nums:
            if n - 1 in numset:
                continue
            cur = n
            cur_seq = 1
            while cur + 1 in numset:
                cur_seq += 1
                cur += 1
            longest = max(longest, cur_seq)
        return longest